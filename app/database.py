from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.app_settings import db_settings


async_engine: AsyncEngine = create_async_engine(db_settings.DATABASE_URL, echo=False)


# async_sessionmaker: a factory for new AsyncSession objects.
# expire_on_commit - don't expire objects after transaction commit
# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
