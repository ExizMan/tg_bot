import os
import enum
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler
from depends import bot_repository

token = ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_id = update.message.from_user.id
    await bot_repository.insert_user(telegram_id)
    await update.message.reply_text("Hi! Which task would you like to do? Which tasks already done?")


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    await bot_repository.insert_todo(update.message.from_user.id, text)
    await update.message.reply_text(f"Added: {text}")


async def get(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    todos = bot_repository.get_todos(update.message.from_user.id)
    if not todos:
        await update.message.reply_text("You don't have any tasks")
    else:
        await update.message.reply_text("\n".join(todos))
    ...


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    todo_id = context.args[0]
    await bot_repository.delete_todo(user_id, todo_id)


class EnumTodos(enum.Enum):
    ADD_TODO = 1
    GET_TODOS = 2
    DELETE_TODO = 3


def main() -> None:
    application = Application.builder().token(token).build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            EnumTodos.ADD_TODO: [CommandHandler("add", add)],
            EnumTodos.GET_TODOS: [CommandHandler("get", get)],
            EnumTodos.DELETE_TODO: [CommandHandler("delete", delete)],
        },
        fallbacks=[CommandHandler("start", start)],

    )
    application.add_handler(conversation_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
