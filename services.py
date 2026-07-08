from telegram import InputMediaPhoto
from telegram import Update
from telegram.ext import ContextTypes
from keyboards import (
    main_keyboard,
    services_keyboard,
    roof_keyboard,
    waterproof_keyboard,
    repair_keyboard,
    application_keyboard,
)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text

    if msg == "🏠 Наши услуги":

        await update.message.reply_text(
            "Выберите интересующий раздел:",
            reply_markup=services_keyboard,
        )
    elif msg == "📸 Галерея работ":

        media = [
            InputMediaPhoto(media=open("фото/1.jpg", "rb")),
        ]

        await update.message.reply_media_group(media)
        await update.message.reply_text(
            "🏠 Наши выполненные работы\n\n"
            "✅ Монтаж скатных кровель\n"
            "✅ Металлочерепица\n"
            "✅ Гибкая черепица\n"
            "✅ Стропильные системы\n"
            "✅ Монтаж под ключ\n\n"
            "📞 Для расчёта стоимости нажмите кнопку «📝 Оставить заявку»."
        )

    elif msg == "🏡 Скатная кровля":
        await update.message.reply_text(
            "🏡 СКАТНАЯ КРОВЛЯ\n\n"
            "Выберите интересующий вид:",
            reply_markup=roof_keyboard,
        )
    elif msg == "🏠 Каркасные дома":
        await update.message.reply_text(
        "🏠 КАРКАСНЫЕ ДОМА\n\n"
        "✔ Строительство каркасных домов под ключ\n"
        "✔ Монтаж силового каркаса\n"
        "✔ Утепление и пароизоляция\n"
        "✔ Монтаж кровли\n"
        "✔ Наружная и внутренняя отделка\n\n"
        "📝 Для расчёта стоимости нажмите «Оставить заявку».",
        reply_markup=application_keyboard,
    )
    elif msg == "🏢 Наплавляемая гидроизоляция":

        await update.message.reply_text(
            "🏢 НАПЛАВЛЯЕМАЯ ГИДРОИЗОЛЯЦИЯ\n\n"
            "Выберите интересующий вид:",
            reply_markup=waterproof_keyboard,
        )

    elif msg == "🔧 Ремонт кровли":

        await update.message.reply_text(
            "🔧 РЕМОНТ КРОВЛИ\n\n"
            "Выберите интересующий вид:",
            reply_markup=repair_keyboard,
        )

    elif msg == "🏠 Металлочерепица":

        await update.message.reply_text(
         "🏡 Металлочерепица\n\n"
         "Монтаж металлочерепицы любой сложности.\n\n"
         "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
         reply_markup=application_keyboard,
        )

    elif msg == "🏠 Профнастил":

        await update.message.reply_text(
            "🏡 Профнастил\n\n"
            "Монтаж кровли из профнастила.",
            reply_markup=application_keyboard,
        )

    elif msg == "🏠 Гибкая черепица":

        await update.message.reply_text(
            "🏡 Гибкая черепица\n\n"
            "Монтаж мягкой кровли.",
         reply_markup=application_keyboard,
        )

    elif msg == "🏠 Композитная черепица":

        await update.message.reply_text(
            "🏡 Композитная черепица\n\n"
            "Монтаж композитной кровли.",
         reply_markup=application_keyboard,
        )

    elif msg == "🏠 Фальцевая кровля":

        await update.message.reply_text(
         "🏡 Фальцевая кровля\n\n"
         "Монтаж фальцевой кровли.",
         reply_markup=application_keyboard,
        )
    elif msg == "🪟 Установка мансардных окон":

        await update.message.reply_text(
         "🪟 УСТАНОВКА МАНСАРДНЫХ ОКОН\n\n"
         "✔ Монтаж мансардных окон любой сложности\n"
         "✔ Установка в готовую кровлю\n"
         "✔ Установка при строительстве новой кровли\n"
         "✔ Герметизация и утепление\n"
         "✔ Гарантия на выполненные работы\n\n"
         "📝 Для расчёта стоимости нажмите «Оставить заявку».",
         reply_markup=application_keyboard,
        )
    elif msg == "🏢 Наплавление стен":

        await update.message.reply_text(
        "🏢 НАПЛАВЛЕНИЕ СТЕН\n\n"
        "✔ Наплавляемая гидроизоляция стен\n"
        "✔ Защита от влаги и протечек\n"
        "✔ Работаем с частными и коммерческими объектами\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🏢 Монтаж пароизоляции":

        await update.message.reply_text(
        "🏢 МОНТАЖ ПАРОИЗОЛЯЦИИ\n\n"
        "✔ Монтаж пароизоляции\n"
        "✔ Устройство кровельного пирога\n"
        "✔ Соблюдение технологии монтажа\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🏢 Монтаж наплавляемой гидроизоляции":

        await update.message.reply_text(
        "🏢 НАПЛАВЛЯЕМАЯ ГИДРОИЗОЛЯЦИЯ\n\n"
        "✔ Монтаж наплавляемой гидроизоляции\n"
        "✔ Плоские кровли любой сложности\n"
        "✔ Гарантия качества выполненных работ\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🏢 Установка аэраторов":

        await update.message.reply_text(
        "🏢 УСТАНОВКА АЭРАТОРОВ\n\n"
        "✔ Монтаж кровельных аэраторов\n"
        "✔ Улучшение вентиляции кровли\n"
        "✔ Продление срока службы кровли\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🏢 Монтаж кровельных воронок":

        await update.message.reply_text(
        "🏢 МОНТАЖ КРОВЕЛЬНЫХ ВОРОНОК\n\n"
        "✔ Монтаж внутренних водостоков\n"
        "✔ Установка кровельных воронок\n"
        "✔ Надёжный отвод дождевой и талой воды\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🔧 Устранение протечек":

        await update.message.reply_text(
        "🔧 УСТРАНЕНИЕ ПРОТЕЧЕК\n\n"
        "✔ Поиск причины протечки\n"
        "✔ Ремонт кровельного покрытия\n"
        "✔ Герметизация проблемных участков\n"
        "✔ Гарантия на выполненные работы\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🔧 Монтаж шахт":

        await update.message.reply_text(
        "🔧 МОНТАЖ ШАХТ\n\n"
        "✔ Монтаж вентиляционных и дымовых шахт\n"
        "✔ Герметизация примыканий\n"
        "✔ Соблюдение строительных норм\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🔧 Установка водосточной системы":

        await update.message.reply_text(
        "🔧 УСТАНОВКА ВОДОСТОЧНОЙ СИСТЕМЫ\n\n"
        "✔ Монтаж желобов и труб\n"
        "✔ Установка водосточной системы под ключ\n"
        "✔ Надёжный отвод дождевой воды\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "🔧 Облицовка софитов":

        await update.message.reply_text(
        "🔧 ОБЛИЦОВКА СОФИТОВ\n\n"
        "✔ Монтаж софитов\n"
        "✔ Подшивка карнизных свесов\n"
        "✔ Аккуратная отделка и долговечные материалы\n\n"
        "📝 Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=application_keyboard,
        )
    elif msg == "💰 Цены":

        await update.message.reply_text(
        "💰 ПРАЙС НА УСЛУГИ\n\n"

        "🏡 СКАТНАЯ КРОВЛЯ\n"
        "• Металлочерепица — от 900 ₽/м²\n"
        "• Профнастил — от 850 ₽/м²\n"
        "• Гибкая черепица — от 1200 ₽/м²\n"
        "• Композитная черепица — от 1500 ₽/м²\n"
        "• Фальцевая кровля — от 1600 ₽/м²\n\n"

        "🏢 НАПЛАВЛЯЕМАЯ ГИДРОИЗОЛЯЦИЯ\n"
        "• Наплавление кровли — от 700 ₽/м²\n"
        "• Наплавление стен — от 800 ₽/м²\n"
        "• Пароизоляция — от 250 ₽/м²\n"
        "• Кровельный пирог — от 1200 ₽/м²\n"
        "• Установка аэраторов — от 2500 ₽/шт\n"
        "• Монтаж кровельных воронок — от 3000 ₽/шт\n\n"

        "🔧 РЕМОНТ КРОВЛИ\n"
        "• Устранение протечек — от 5000 ₽\n"
        "• Замена участка кровли — от 1000 ₽/м²\n"
        "• Монтаж шахт — от 7000 ₽\n"
        "• Монтаж водосточной системы — от 700 ₽/п.м.\n"
        "• Облицовка софитов — от 700 ₽/п.м.\n\n"

        "📞 Итоговая стоимость рассчитывается после осмотра объекта.\n\n"
        "📝 Для получения точного расчета нажмите «Оставить заявку»."
        )
    elif msg == "⬅️ Назад":

        await update.message.reply_text(
            "Главное меню",
            reply_markup=main_keyboard,
        )

    return