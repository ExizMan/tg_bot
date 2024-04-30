from sqlalchemy import select

from databases.database import Database, async_engine
from databases.models import Users, Todos


class AsyncQueries:
    @staticmethod
    async def create_or_replace_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Database.metadata.drop_all)
            await conn.run_sync(Database.metadata.create_all)

    @staticmethod
    async def insert_user(telegram_id: int):
        async with async_engine.begin() as session:
            if await session.execute(select(Users).where(Users.telegram_id == telegram_id)):
                return
            session.add(Users(telegram_id=telegram_id))
            await session.flush()
            await session.commit()

    @staticmethod
    async def insert_todo(user_id: int, task: str):
        async with async_engine.begin() as session:
            session.add(Todos(user_id=user_id, task=task))
            await session.flush()
            await session.commit()

    async def get_todos(self, user_id: int):
        async with async_engine.begin() as session:
            query = select(Todos).where(Todos.user_id == user_id)
            todos = await session.execute(query)
            todos = todos.scalars().all()
            return todos

    async def delete_todo(self, user_id: int, todo_id: int):
        async with async_engine.begin() as session:
            query = select(Todos).where(Todos.user_id == user_id, Todos.todo_id == todo_id)
            todo = await session.execute(query)
            todo = todo.scalars().first()
            await session.delete(todo)
            await session.commit()


queries = {"AsyncQueries": AsyncQueries()}
