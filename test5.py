
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5891863496:AAG5t31e8Rq8KVjHhgCHPTcqL8rImjTQcNo").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()