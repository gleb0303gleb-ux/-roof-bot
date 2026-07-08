from telegram import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    [
        ["🏠 Наши услуги"],
        ["📸 Галерея работ"],
        ["📝 Оставить заявку"],
    ],
    resize_keyboard=True,
)

services_keyboard = ReplyKeyboardMarkup(
    [
        ["🏡 Скатная кровля"],
        ["🏠 Каркасные дома"],
        ["🏢 Наплавляемая гидроизоляция"],
        ["🔧 Ремонт кровли"],
        ["⬅️ Назад"],
    ],
    resize_keyboard=True,
)

roof_keyboard = ReplyKeyboardMarkup(
    [
    ["🏠 Металлочерепица"],
    ["🏠 Профнастил"],
    ["🏠 Гибкая черепица"],
    ["🏠 Композитная черепица"],
    ["🏠 Фальцевая кровля"],
    ["🪟 Установка мансардных окон"],
    ["📝 Оставить заявку"],
    ["⬅️ Назад"],
],
    resize_keyboard=True,
)

waterproof_keyboard = ReplyKeyboardMarkup(
    [
        ["🏢 Наплавление стен"],
        ["🏢 Монтаж пароизоляции"],
        ["🏢 Монтаж наплавляемой гидроизоляции"],
        ["🏢 Установка аэраторов"],
        ["🏢 Монтаж кровельных воронок"],
        ["📝 Оставить заявку"],
        ["⬅️ Назад"],
    ],
    resize_keyboard=True,
)
repair_keyboard = ReplyKeyboardMarkup(
    [
        ["🔧 Устранение протечек"],
        ["🔧 Монтаж шахт"],
        ["🔧 Установка водосточной системы"],
        ["🔧 Облицовка софитов"],
        ["📝 Оставить заявку"],
        ["⬅️ Назад"],
    ],
    resize_keyboard=True,
)
from telegram import ReplyKeyboardMarkup

application_keyboard = ReplyKeyboardMarkup(
    [
        ["📝 Оставить заявку"],
        ["⬅️ Назад"],
    ],
    resize_keyboard=True,
)