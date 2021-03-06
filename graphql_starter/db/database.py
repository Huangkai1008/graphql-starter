from tortoise import Tortoise

from graphql_starter.core.config import (
    DB_TYPE,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DATABASE,
)

DB_URL = f'{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}'


async def init():
    """初始化连接"""
    await Tortoise.init(
        db_url=DB_URL,
        modules={'db': ['graphql_starter.db.link', 'graphql_starter.db.user']},
    )
    await Tortoise.generate_schemas()


async def disconnect():
    """停止连接"""
    await Tortoise.close_connections()
