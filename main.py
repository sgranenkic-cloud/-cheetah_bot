import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

VERSION = os.environ.get("RAILWAY_DEPLOYMENT_ID", "local")

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")

keyboard = [
    ["Стать настоящим гепардом"],
    ["Что нужно, чтобы начать бегать?"],
    ["Где проходят занятия"],
    ["Какая стоимость занятий"],
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Жмяк на кнопку в меню и начинаем!\n\nВерсия: {VERSION}",
        reply_markup=reply_markup,
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Какая стоимость занятий":
        await update.message.reply_text(
            "Тарифы:\n"
            "• Групповые занятия — 8 900 ₽/мес.\n"
            "• Дистанционное ведение — 8 400 ₽/мес.\n\n"
            f"Версия: {VERSION}"
        )

    elif text == "Где проходят занятия":
        await update.message.reply_text(
            "Занятия проходят на стадионе и в парке.\n\n"
            f"Версия: {VERSION}"
        )

    elif text == "Что нужно, чтобы начать бегать?":
        await update.message.reply_text(
            "Кроссовки, желание и немного дисциплины 🙂\n\n"
            f"Версия: {VERSION}"
        )

    elif text == "Стать настоящим гепардом":
        await update.message.reply_text(
            "Напиши нам в личные сообщения и мы расскажем подробнее!\n\n"
            f"Версия: {VERSION}"
        )

    else:
        await update.message.reply_text(
            f"Выбери пункт из меню 👇\n\nВерсия: {VERSION}"
        )

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info(f"Bot starting... Version: {VERSION}")
    application.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
