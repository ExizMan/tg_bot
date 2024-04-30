import asyncio

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from databases.config import posgres_async_config

async_engine = create_async_engine(
    url=posgres_async_config.POSTGRES_URL,
    echo=True,
)

async_factory = async_sessionmaker(async_engine)

class Database(DeclarativeBase):
    pass