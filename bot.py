from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7386747475:AAHKaQ37fCEhlb628U7DlJWIwgWAp1po5eg"

# پیام خوش‌آمد و منوی اصلی
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧾 خرید اشتراک", callback_data='buy')],
        [InlineKeyboardButton("📘 آموزش اتصال", callback_data='howto')],
        [InlineKeyboardButton("🛠 پشتیبانی", url="https://t.me/Psycho_remix1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌟 خوش آمدید به ربات فروش فیلترشکن امن و پرسرعت 💎\n\n"
        "از منوی زیر انتخاب کنید 👇",
        reply_markup=reply_markup
    )

# مدیریت دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'buy':
        keyboard = [
            [InlineKeyboardButton("۱ کاربره نامحدود - ۹۹ هزار", callback_data='plan1')],
            [InlineKeyboardButton("۲ کاربره نامحدود - ۱۱۵ هزار", callback_data='plan2')],
            [InlineKeyboardButton("۳ کاربره نامحدود - ۱۶۹ هزار", callback_data='plan3')],
            [InlineKeyboardButton("🔙 بازگشت", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("لطفاً یکی از پلن‌ها را انتخاب کنید 👇", reply_markup=reply_markup)

    elif query.data == 'plan1':
        await query.edit_message_text(
            "✅ پلن انتخابی: ۱ کاربره نامحدود - ۹۹ هزار تومان\n"
            "💳 6277 6013 6877 6066 - بنام رضوانی\n\n"
            "سپس عکس فیش واریزی را ارسال کنید تا سفارش شما بررسی شود."
        )
    elif query.data == 'plan2':
        await query.edit_message_text(
            "✅ پلن انتخابی: ۲ کاربره نامحدود - ۱۱۵ هزار تومان\n"
            "💳 6277 6013 6877 6066 - بنام رضوانی\n\n"
            "سپس عکس فیش واریزی را ارسال کنید."
        )
    elif query.data == 'plan3':
        await query.edit_message_text(
            "✅ پلن انتخابی: ۳ کاربره نامحدود - ۱۶۹ هزار تومان\n"
            "💳 6277 6013 6877 6066 - بنام رضوانی\n\n"
            "سپس عکس فیش واریزی را ارسال کنید."
        )
    elif query.data == 'howto':
        await query.edit_message_text(
            "📘 آموزش اتصال:\n\n"
            "1️⃣ برنامه NapsternetV یا v2ray را نصب کنید.\n"
            "2️⃣ کانفیگی که برایتان ارسال می‌شود را وارد کنید.\n"
            "3️⃣ اتصال را فعال کنید.\n\n"
            "در صورت سوال با پشتیبانی تماس بگیرید: @Psycho_remix1"
        )
    elif query.data == 'back':
        await start(query, context)

# اجرای بات
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == '__main__':
    main()
