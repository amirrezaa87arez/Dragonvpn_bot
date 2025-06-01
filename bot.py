import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")  # توکن از محیط گرفته میشه

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

def main():
    from flask import Flask, request
    import asyncio

    app = Flask(__name__)
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    @app.route(f"/webhook/{TOKEN}", methods=["POST"])
    async def webhook():
        await application.update_queue.put(Update.de_json(request.get_json(force=True), application.bot))
        return "OK"

    @app.route("/")
    def index():
        return "Bot is running!"

    # ست کردن webhook
    async def set_webhook():
        await application.bot.set_webhook(f"https://dragonvpn-bot.onrender.com/webhook/{TOKEN}")

    loop = asyncio.get_event_loop()
    loop.create_task(set_webhook())

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

if __name__ == "__main__":
    main()
