from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from keyboards import *
from states import *
from config import ADMIN_ID


user_data = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать в KrovSHAR!\n\n"
        "Профессиональная кровля и гидроизоляция.\n\n"
        "Выберите нужный раздел.",
        reply_markup=main_keyboard
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "🏠 Наши услуги":
        await update.message.reply_text(
            "Выберите услугу:",
            reply_markup=services_keyboard
        )

    elif text == "🏠 Скатная кровля":
        await update.message.reply_text(
            "Выберите тип кровли:",
            reply_markup=roof_keyboard
        )

    elif text == "🧱 Наплавляемая гидроизоляция":
        await update.message.reply_text(
            "Выберите раздел:",
            reply_markup=waterproof_keyboard
        )

    elif text == "🔧 Ремонт кровли":
        await update.message.reply_text(
            "Выберите раздел:",
            reply_markup=repair_keyboard
        )

    elif text == "📸 Галерея работ":
        await update.message.reply_text(
            "📷 Здесь будут фотографии ваших объектов."
        )

    elif text == "💰 Цены":
        await update.message.reply_text(
            "Стоимость рассчитывается индивидуально.\n\n"
            "Нажмите «📝 Оставить заявку», и мы подготовим смету."
        )

    elif text == "☎️ Контакты":
        await update.message.reply_text(
            "📞 Телефон:\n"
            "+7 XXX XXX XX XX\n\n"
            "✉️ Email:\n"
            "info@krovshar.ru"
        )

    elif text == "📝 Оставить заявку":

        await update.message.reply_text(
            "Как вас зовут?"
        )

        return NAME

    elif text == "⬅️ Назад":
        await update.message.reply_text(
            "Главное меню",
            reply_markup=main_keyboard
        )

    return ConversationHandler.END
    async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_data["name"] = update.message.text

    await update.message.reply_text(
        "📞 Введите номер телефона:"
    )

    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_data["phone"] = update.message.text

    await update.message.reply_text(
        "🏠 Какая услуга вас интересует?\n\n"
        "Например:\n"
        "• Металлочерепица\n"
        "• Гидроизоляция\n"
        "• Ремонт кровли"
    )

    return SERVICE


async def get_service(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_data["service"] = update.message.text

    await update.message.reply_text(
        "💬 Опишите задачу:"
    )

    return COMMENT


async def get_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_data["comment"] = update.message.text

    await update.message.reply_text(
        "📷 Если есть фотографии объекта — отправьте их.\n\n"
        "Если фотографий нет, напишите слово:\n\n"
        "Пропустить"
    )

    return PHOTO
    async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.photo:

        photo = update.message.photo[-1]

        file = await photo.get_file()

        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=file.file_id
        )

    text = f"""
🔥 НОВАЯ ЗАЯВКА

👤 Имя:
{user_data['name']}

📞 Телефон:
{user_data['phone']}

🏠 Услуга:
{user_data['service']}

💬 Комментарий:
{user_data['comment']}
"""

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=text
    )

    await update.message.reply_text(
        "✅ Спасибо!\n\n"
        "Ваша заявка успешно отправлена.\n"
        "Мы свяжемся с вами в ближайшее время.",
        reply_markup=main_keyboard
    )

    user_data.clear()

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_data.clear()

    await update.message.reply_text(
        "Главное меню",
        reply_markup=main_keyboard
    )

    return ConversationHandler.END
     