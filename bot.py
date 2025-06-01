from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from flask import Flask, request

TOKEN = os.getenv("7386747475:AAHKaQ37fCEhlb628U7DlJWIwgWAp1po5eg")  # در Render از طریق Environment Variable ست کن
APP_URL = os.getenv("https://dragonvpn-bot.onrender.com")  # مثل: https://your-app-name.onrender.com

app = Flask(__name__)

# تنظیمات ربات تلگرام
telegram_app = Application.builder().token(TOKEN).build()

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
            "💳 6277 6013 6877 6066 - بنام رضوانی\n"
            "سپس عکس فیش واریزی را ارسال کنید."
        )
    elif query.data == 'plan3':
        await query.edit_message_text(
            "✅ پلن انتخابی: ۳ کاربره نامحدود - ۱۶۹ هزار تومان\n"
            "💳 6277 6013 6877 6066 - بنام رضوانی\n"
            "سپس عکس فیش واریزی را ارسال کنید."
        )
    elif query.data == 'back':
        await start(update, context)

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CallbackQueryHandler(button))

# روت وب‌هوک
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    telegram_app.update_queue.put_nowait(Update.de_json(request.get_json(force=True), telegram_app.bot))
    return "ok", 200

# راه‌اندازی وب‌هوک هنگام اجرا
@app.before_first_request
def setup_webhook():
    from telegram import Bot
    bot = Bot(token=TOKEN)
    bot.delete_webhook()
    bot.set_webhook(url=f"{APP_URL}/{TOKEN}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
