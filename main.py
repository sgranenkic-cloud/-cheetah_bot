
import os
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "grondkind")  # set via env if needed

router = Router()

def main_kb():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="Стать настоящим гепардом")],
            [KeyboardButton(text="Что нужно, чтобы начать бегать?")],
            [KeyboardButton(text="Где проходят занятия")],
            [KeyboardButton(text="Какая стоимость занятий")],
        ],
    )

@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer(
        "Привет! Я бот Cheetah.Club.\nВыбери, чем помочь:",
        reply_markup=main_kb()
    )

@router.message(F.text == "Стать настоящим гепардом")
async def become_cheetah(msg: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Записаться через форму",
            url="https://forms.yandex.ru/u/6705fa6c505690f108fe691d/"
        )],
        [InlineKeyboardButton(
            text="Написать администратору",
            url=f"https://t.me/{ADMIN_USERNAME}"
        )],
    ])
    text = (
        "Хочешь в стаю Cheetah.Club? Заполняй форму или напиши администратору — "
        "поможем выбрать первую тренировку и формат."
    )
    await msg.answer(text, reply_markup=kb)

@router.message(F.text == "Что нужно, чтобы начать бегать?")
async def newbie(msg: Message):
    text = (
        "Мини-чеклист новичка:\n"
        "• Кроссовки для бега, футболка/шорты из синтетики.\n"
        "• Часы, фиксирующие тренировки — по возможности.\n"
        "• Отсутствие мед. противопоказаний.\n"
        "• Желание стать лучше — обязательно."
    )
    await msg.answer(text)

@router.message(F.text == "Где проходят занятия")
async def places(msg: Message):
    text = (
        "Расписание групп:\n"
        "• Среда 19:00 — Стадион СГУПС.\n"
        "• Четверг 18:00 — Стадион НГУ (группа Академа).\n"
        "• Воскресенье 10:00 — совместная тренировка двух групп "
        "(Локомотив / Дендропарк / ЛДС Арена — по объявлению).\n"
        "• Дистанционно — в любое время и в любом месте."
    )
    await msg.answer(text)

@router.message(F.text == "Какая стоимость занятий")
async def prices(msg: Message):
    text = (
        "Тарифы:\n"
        "• Групповые занятия — 8 400 ₽/мес.\n"
        "• Дистанционное ведение — 7 700 ₽/мес."
    )
    await msg.answer(text)

async def run():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    if not BOT_TOKEN:
        raise SystemExit("ENV BOT_TOKEN is required")
    asyncio.run(run())
