from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

TOKEN = "7386747475:AAHKaQ37fCEhlb628U7DlJWIwgWAp1po5eg"  # توکن رباتت رو اینجا بذار

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧾 خرید اشتراک", callback_data='buy')],
        [InlineKeyboardButton("📘 آموزش اتصال", url="https://t.me/amuzesh_dragonvpn")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌟 خوش آمدید به ربات فروش فیلترشکن امن و پرسرعت 💎\n\n"
        "از منوی زیر انتخاب کنید 👇",
        reply_markup=reply_markup
    )

# دکمه‌های callback
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
    elif query.data == 'back':
        await start(update, context)

# پاسخ به پیام‌های متنی مثل منوی کیبورد پایین
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "آموزش اتصال" in text:
        await update.message.reply_text(
            "📘 آموزش اتصال:\n"
            "۱. برنامه NapsternetV یا v2ray را نصب کنید\n"
            "۲. کانفیگی که برایتان ارسال می‌شود را وارد کنید\n"
            "۳. اتصال را فعال کنید\n\n"
            "⚠️ هر سوالی داشتید با پشتیبانی تماس بگیرید:\n@Psycho_remix1"
        )
    elif "خرید اشتراک" in text:
        await update.message.reply_text(
            "✅ پلن انتخابی: ۱ کاربره نامحدود - ۹۹ هزار تومان\n"
            "💳 6277 6013 6877 6066 - بنام رضوانی\n\n"
            "سپس عکس فیش واریزی را ارسال کنید تا سفارش شما بررسی شود."
        )
    elif "پشتیبانی" in text:
        await update.message.reply_text(
            "🛠 برای پشتیبانی به آیدی زیر پیام دهید:\n@Psycho_remix1"
        )

# شروع اپلیکیشن
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    app.run_polling()

if __name__ == '__main__':
    main()
