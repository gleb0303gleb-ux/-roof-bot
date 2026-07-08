from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

from config import TOKEN

from keyboards import (
    main_keyboard,
)

from services import menu

from application import (
    NAME,
    PHONE,
    SERVICE,
    COMMENT,
    start_application,
    get_name,
    get_phone,
    get_service,
    get_comment,
    cancel,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👋 Добро пожаловать в KrovSHAR!\n\n"
        "Профессиональная кровля, гидроизоляция и ремонт кровли.\n\n"
        "Выберите нужный раздел.",
        reply_markup=main_keyboard,
    )


application_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Regex("^📝 Оставить заявку$"),
            start_application,
        ),
    ],

    states={

        NAME: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_name,
            )
        ],

        PHONE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_phone,
            )
        ],

        SERVICE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_service,
            )
        ],

        COMMENT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_comment,
            )
        ],

    },

    fallbacks=[
        CommandHandler(
            "cancel",
            cancel,
        )
    ],
)
app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler(
        "start",
        start,
    )
)

app.add_handler(application_handler)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        menu,
    )
)

print("✅ Бот запущен...")

app.run_polling()