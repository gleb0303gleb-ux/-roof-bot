from telegram import ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from keyboards import main_keyboard
from config import ADMIN_ID

NAME, PHONE, SERVICE, COMMENT = range(4)


async def start_application(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
    "👤 Как вас зовут?",
    reply_markup=ReplyKeyboardRemove(),
    )

    return NAME


async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    name = update.message.text.strip()

    if len(name) < 2 or any(ch.isdigit() for ch in name):
        await update.message.reply_text(
            "❌ Пожалуйста, введите корректное имя."
        )
        return NAME

    context.user_data["name"] = name

    await update.message.reply_text(
        "📞 Введите номер телефона:"
    )

    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):

    phone = update.message.text.strip()

    phone_check = (
        phone.replace("+", "")
        .replace(" ", "")
        .replace("-", "")
        .replace("(", "")
        .replace(")", "")
    )

    if not phone_check.isdigit():
        await update.message.reply_text(
            "❌ Введите корректный номер телефона."
        )
        return PHONE

    context.user_data["phone"] = phone

    await update.message.reply_text(
        "🏠 Какая услуга вас интересует?"
    )

    return SERVICE


async def get_service(update: Update, context: ContextTypes.DEFAULT_TYPE):

    service = update.message.text.strip()

    if (
        len(service) < 2
        or service in [
            "🏠 Наши услуги",
            "📸 Галерея работ",
            "📝 Оставить заявку",
            "⬅️ Назад",
        ]
    ):
        await update.message.reply_text(
            "❌ Напишите название интересующей услуги."
        )
        return SERVICE

    context.user_data["service"] = service

    await update.message.reply_text(
        "💬 Оставьте комментарий:"
    )

    return COMMENT


async def get_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    comment = update.message.text.strip()

    if comment in [
        "🏠 Наши услуги",
        "📸 Галерея работ",
        "📝 Оставить заявку",
        "⬅️ Назад",
    ]:
        await update.message.reply_text(
            "❌ Напишите комментарий текстом."
        )
        return COMMENT

    context.user_data["comment"] = comment

    text = (
        "📥 НОВАЯ ЗАЯВКА\n\n"

        f"👤 Имя: {context.user_data['name']}\n"
        f"📞 Телефон: {context.user_data['phone']}\n"
        f"🏠 Услуга: {context.user_data['service']}\n"
        f"💬 Комментарий: {context.user_data['comment']}"
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=text
    )
    print("ADMIN_ID =", ADMIN_ID)
    print(text)
    await update.message.reply_text(
        "✅ Спасибо!\n\n"
        "Ваша заявка отправлена.\n"
        "Мы свяжемся с вами в ближайшее время.",
        reply_markup=main_keyboard
    )

    context.user_data.clear()

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.clear()

    await update.message.reply_text(
        "Главное меню",
        reply_markup=main_keyboard
    )

    return ConversationHandler.END