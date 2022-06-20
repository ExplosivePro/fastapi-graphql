from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from schema import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/graphql", graphql_app)
@app.get('/')
def ping():
    return {'ping': 'pong'}