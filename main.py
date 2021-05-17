from time import sleep, time_ns
from requests import post, get, patch
from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from flask_graphql import GraphQLView
from lib.schema import schema
from lib.authorization import Authorization
from lib.populate_db import populate
from dotenv import load_dotenv
from os import getenv

load_dotenv()


app = Flask(__name__)
CORS(app)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,
        pretty=True,
        middleware={Authorization()},
    ),
)

MAX_RETRIES = int(getenv("GATEWAY_RETRIES"))


def establish_gateway_connection(attempts=0):
    if attempts >= MAX_RETRIES:
        return

    name = "graphql"
    upstream_name = f"{name}_upstream"
    base_url = f'http://{getenv("GATEWAY")}'
    service_url = f"{base_url}/services/{name}"
    upstream_url = f"{base_url}/upstreams/{upstream_name}"

    try:
        service_res = get(url=service_url)

        if service_res.status_code == 404:
            # Create the Kong service
            post(
                url=f"{base_url}/services",
                data={"name": name, "url": base_url},
            )
            print("Kong: Service created")
            # Create the upstream
            post(url=f"{base_url}/upstreams", data={"name": upstream_name})
            print("Kong: Upstream created")
            # Link upstream
            patch(url=service_url, data={"host": upstream_name})
            print("Kong: Upstream linked")
            # Create the route
            req = post(
                url=f"{service_url}/routes",
                data={"name": name, "paths[]": "/graphql", "strip_path": "false"},
            )
            print(req.url)
            print(req.status_code)
            print(req.json())
            print("Kong: Route added")

        # Add target
        res = post(
            url=f"{upstream_url}/targets", data={"target": getenv("GRAPHQL_URL")}
        )

        if res.status_code == 200 or res.status_code == 409:
            print("Kong: Connection established")
            return

    except:
        print("Gateway is not available!")

    sleep(0.2)
    establish_gateway_connection(attempts=attempts + 1)


if __name__ == "__main__":
    db = connect(
        "RepoAdopt", host=getenv("HOST"), port=getenv("DBPORT"), alias="default"
    )
    if getenv("ENVIRONMENT") == "develop":
        db.drop_database("RepoAdopt")
        populate()

    establish_gateway_connection()

    app.run(debug=True, host="0.0.0.0", port=getenv("PORT"))
