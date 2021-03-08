from flask import Flask
from mongoengine import connect
from flask_graphql import GraphQLView
from lib.adoptableSchema import schema

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
    pretty=True,
))


if __name__ == '__main__':
    connect('RepoAdopt', host='mongodb://localhost/', port=27017, alias='default')
    app.run(debug=True, host='0.0.0.0', port=5000)
