from time import sleep, time_ns
from requests import post
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


def establish_gateway_connection():
    base_url = f'http://{getenv("GATEWAY")}/services'
    name = "graphql"
    try:
        res = post(
            url=base_url,
            data={"name": name, "url": getenv("GRAPHQL_URL")},
        )

        if res.status_code == 201:
            post(
                url=f"{base_url}/{name}/routes",
                data={"name": name, "paths[]": "/graphql"},
            )

            print("Created gateway connection!")

            return
        elif res.status_code == 409:
            print("Gateway connection already created!")
        else:
            print("Could not create gateway connection!")

    except:
        print("Gateway is not available!")

    sleep(time_ns=200)
    establish_gateway_connection()


if __name__ == "__main__":
    db = connect(
        "RepoAdopt", host=getenv("HOST"), port=getenv("DBPORT"), alias="default"
    )
    if getenv("ENVIRONMENT") == "develop":
        db.drop_database("RepoAdopt")
        populate()

    establish_gateway_connection()

    app.run(debug=True, host="0.0.0.0", port=getenv("PORT"))
