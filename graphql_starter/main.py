import uvicorn

from fastapi import FastAPI
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from graphql_starter.db import database
from graphql_starter.core.config import PROJECT_NAME
from graphql_starter.schema.link import schema

app = FastAPI(title=PROJECT_NAME)
app.add_route("/graphql", GraphQLApp(schema=schema, executor=AsyncioExecutor()))


@app.on_event('startup')
async def startup() -> None:
    await database.init()


@app.on_event('shutdown')
async def shutdown() -> None:
    await database.disconnect()


uvicorn.run(app, host='0.0.0.0', port=4000)
