from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

YOUR_TOKEN_HERE = '5891863496:AAF2MemwhNDKNBX3Ok7BcBwmC48SXHj4C6s'

app = ApplicationBuilder().token(YOUR_TOKEN_HERE).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()