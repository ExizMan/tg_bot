from databases.queries import queries

AsyncQueries = queries["AsyncQueries"]
class BotRepository:
    def __init__(self, Repository: AsyncQueries):
        self.Repository = Repository

    async def insert_user(self, telegram_id: int):
        await self.Repository.insert_user(telegram_id)

    async def insert_todo(self, user_id: int, task: str):
        await self.Repository.insert_todo(user_id, task)

    async def get_todos(self, user_id: int):
        return await self.Repository.get_todos(user_id)

    async def delete_todo(self, user_id: int, todo_id: int):
        await self.Repository.delete_todo(user_id, todo_id)


bot_repository = BotRepository(AsyncQueries)