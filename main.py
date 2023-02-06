# coding: utf-8
import requests
import os

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes
)



len_text = [['SBER', 'Сбербанк России ПАО ао'],
            ['SBERP', 'Сбербанк России ПАО ап']]
# len_text = ['one', 'two', 'tree']


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с тремя встроенными кнопками."""
    keyboard = []
    for x in len_text:
        keyboard.append([InlineKeyboardButton(text=x[1], callback_data='1')])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "По введеному {} есть такие эмитенты:",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Разбирает CallbackQuery и обновляет текст сообщения."""
    query = update.callback_query

    # CallbackQueries требуют ответа, даже если уведомление пользователю не требуется
    # В противном случае у некоторых клиентов могут возникнуть проблемы. См. https://core.telegram.org/bots/api#callbackquery 55
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    load_dotenv()

    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
