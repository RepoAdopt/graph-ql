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


if __name__ == "__main__":
    db = connect(
        "RepoAdopt", host=getenv("HOST"), port=getenv("DBPORT"), alias="default"
    )
    if getenv("ENVIRONMENT") == "develop":
        db.drop_database("RepoAdopt")
        populate()
    app.run(debug=True, host="0.0.0.0", port=getenv("PORT"))
