from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

data_base = 'postgresql+asyncpg://name:password@localhost:5432/db'
engine = create_async_engine(data_base)

new_session = async_sessionmaker(engine, expire_on_commit=False)
class Model(DeclarativeBase, MappedAsDataclass):
    pass

async def get_db():
    async with new_session as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_db)]
