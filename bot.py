import os
import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Missing BOT_TOKEN env var")

# --- Texts ---
WELCOME_TEXT = '🐆 Привет!\nТы в боте бегового клуба Cheetah.Club — месте, где пробежки превращаются в привычку, а привычка — в результат.\n\nЗдесь ты можешь:\n▫️ Узнать, как попасть в команду и стать настоящим гепардом.\n▫️ Понять, что нужно для первых шагов в беге.\n▫️ Найти, где проходят наши тренировки.\n▫️ Посмотреть тарифы и формат занятий.\n\nМы тренируем:\n🏃\u200d♀️ От первых  километров до марафона и дальше.\n💬 В Новосибирске и онлайн.\n📅 По расписанию и в удобное тебе время.\n\nЖмяк на кнопку в меню и начинаем!'

JOIN_TEXT = 'Хочешь в стаю Cheetah.Club? Заполняй форму или напиши администратору — поможем выбрать первую тренировку и формат.'

START_RUNNING_TEXT = 'Мини-чеклист новичка:\n• Кроссовки для бега, футболка/шорты из синтетики.\n• Часы, фиксирующие тренировки — по возможности.\n• Отсутствие мед. противопоказаний.\n• Желание стать лучше — обязательно.'

SCHEDULE_TEXT = 'Расписание групп:\n• Среда 19:00 — Манеж ЛДС.\n• Четверг 18:00 — Манеж Кольцово (группа Академа).\n• Воскресенье 10:00 — совместная тренировка двух групп (Манеж Кольцово).\n• Дистанционно — в любое время и в любом месте.'

PRICING_TEXT = 'Тарифы:\n• Групповые занятия — 8 900 ₽/мес.\n• Дистанционное ведение — 8 400 ₽/мес.'

TRAINER_USERNAME = 'grondkind'
FORM_URL = 'https://forms.yandex.ru/u/6705fa6c505690f108fe691d'

# --- UI labels ---
BTN_JOIN = "Стать настоящим гепардом"
BTN_START_RUNNING = "Что нужно, чтобы начать бегать?"
BTN_SCHEDULE = "Где проходят занятия"
BTN_PRICING = "Какая стоимость занятий"

CB_TRAINER = "join:trainer"
CB_FORM = "join:form"


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_JOIN)],
            [KeyboardButton(text=BTN_START_RUNNING)],
            [KeyboardButton(text=BTN_SCHEDULE)],
            [KeyboardButton(text=BTN_PRICING)],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню 👇",
    )


def join_inline_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Написать тренеру",
                    url=f"https://t.me/{TRAINER_USERNAME}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Заполнить форму",
                    url=FORM_URL,
                )
            ],
        ]
    )


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb())


@router.message(F.text == BTN_JOIN)
async def join(message: Message) -> None:
    await message.answer(JOIN_TEXT, reply_markup=join_inline_kb())


@router.message(F.text == BTN_START_RUNNING)
async def start_running(message: Message) -> None:
    await message.answer(START_RUNNING_TEXT, reply_markup=main_menu_kb())


@router.message(F.text == BTN_SCHEDULE)
async def schedule(message: Message) -> None:
    await message.answer(SCHEDULE_TEXT, reply_markup=main_menu_kb())


@router.message(F.text == BTN_PRICING)
async def pricing(message: Message) -> None:
    await message.answer(PRICING_TEXT, reply_markup=main_menu_kb())


@router.message()
async def fallback(message: Message) -> None:
    # If user types something else, just show menu again.
    await message.answer("Выбери пункт в меню 👇", reply_markup=main_menu_kb())


async def main() -> None:
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
