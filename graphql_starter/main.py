import uvicorn

from fastapi import FastAPI

from graphql_starter.db import database
from graphql_starter.core.config import PROJECT_NAME

app = FastAPI(title=PROJECT_NAME)


@app.on_event('startup')
async def startup():
    await database.init()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


uvicorn.run(app, host='0.0.0.0', port=4000)
