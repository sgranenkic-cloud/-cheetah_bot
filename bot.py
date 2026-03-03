import os
import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    raise RuntimeError("Missing BOT_TOKEN env var")

ADMIN_USERNAME = "grondkind"  # without '@'
FORM_URL = "https://forms.yandex.ru/u/6705fa6c505690f108fe691d"

WELCOME_TEXT = (
    "🐆 Привет!\n"
    "Ты в боте бегового клуба Cheetah.Club — месте, где пробежки превращаются в привычку, а привычка — в результат.\n\n"
    "Здесь ты можешь:\n"
    "▫️ Узнать, как попасть в команду и стать настоящим гепардом.\n"
    "▫️ Понять, что нужно для первых шагов в беге.\n"
    "▫️ Найти, где проходят наши тренировки.\n"
    "▫️ Посмотреть тарифы и формат занятий.\n\n"
    "Мы тренируем:\n"
    "🏃‍♀️ От первых  километров до марафона и дальше.\n"
    "💬 В Новосибирске и онлайн.\n"
    "📅 По расписанию и в удобное тебе время.\n\n"
    "Жмяк на кнопку в меню и начинаем!"
)

BECOME_CHEETAH_TEXT = (
    "Хочешь в стаю Cheetah.Club? Заполняй форму или напиши администратору — "
    "поможем выбрать первую тренировку и формат."
)

BEGIN_RUNNING_TEXT = (
    "Мини-чеклист новичка:\n"
    "• Кроссовки для бега, футболка/шорты из синтетики.\n"
    "• Часы, фиксирующие тренировки — по возможности.\n"
    "• Отсутствие мед. противопоказаний.\n"
    "• Желание стать лучше — обязательно."
)

WHERE_TRAININGS_TEXT = (
    "Расписание групп:\n"
    "• Среда 19:00 — Манеж ЛДС.\n"
    "• Четверг 18:00 — Манеж Кольцово (группа Академа).\n"
    "• Воскресенье 10:00 — совместная тренировка двух групп (Манеж Кольцово).\n"
    "• Дистанционно — в любое время и в любом месте."
)

PRICING_TEXT = (
    "Тарифы:\n"
    "• Групповые занятия — 8 900 ₽/мес.\n"
    "• Дистанционное ведение — 8 400 ₽/мес."
)

BTN_BECOME = "Стать настоящим гепардом"
BTN_START = "Что нужно, чтобы начать бегать?"
BTN_WHERE = "Где проходят занятия"
BTN_PRICE = "Какая стоимость занятий"

router = Router()


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_BECOME)],
            [KeyboardButton(text=BTN_START)],
            [KeyboardButton(text=BTN_WHERE)],
            [KeyboardButton(text=BTN_PRICE)],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт в меню",
    )


def become_inline_kb() -> InlineKeyboardMarkup:
    # Bot cannot message @grondkind directly; we provide a deep-link to open chat.
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Написать тренеру", url=f"https://t.me/{ADMIN_USERNAME}")],
            [InlineKeyboardButton(text="Заполнить форму", url=FORM_URL)],
        ]
    )


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb())


@router.message(F.text == BTN_BECOME)
async def become_cheetah(message: Message) -> None:
    await message.answer(BECOME_CHEETAH_TEXT, reply_markup=become_inline_kb())


@router.message(F.text == BTN_START)
async def begin_running(message: Message) -> None:
    await message.answer(BEGIN_RUNNING_TEXT, reply_markup=main_menu_kb())


@router.message(F.text == BTN_WHERE)
async def where_trainings(message: Message) -> None:
    await message.answer(WHERE_TRAININGS_TEXT, reply_markup=main_menu_kb())


@router.message(F.text == BTN_PRICE)
async def pricing(message: Message) -> None:
    await message.answer(PRICING_TEXT, reply_markup=main_menu_kb())


@router.message()
async def fallback(message: Message) -> None:
    await message.answer("Выбери пункт в меню 👇", reply_markup=main_menu_kb())


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
