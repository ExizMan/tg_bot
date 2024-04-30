from sqlalchemy import ForeignKey

from databases.database import Database
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Users(Database):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    # extend with other fields if needed

class Todos(Database):
    __tablename__ = "todos"

    todo_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id", ondelete="CASCADE"))
    task: Mapped[str]