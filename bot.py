
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# دکمه‌ها
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("💳 خرید اشتراک", "📚 آموزش اتصال").add("🛠 پشتیبانی")

plans_menu = ReplyKeyboardMarkup(resize_keyboard=True)
plans_menu.add("۱ کاربره - ۹۹ هزار", "۲ کاربره - ۱۱۵ هزار", "۳ کاربره - ۱۶۹ هزار").add("🔙 بازگشت")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        f"🌟 خوش آمدید به ربات فروش فیلترشکن امن و پرسرعت 💎\n"
        f"برند: Dragon VPN\n\n"
        f"از منوی زیر انتخاب کنید 👇",
        reply_markup=main_menu
    )

@dp.message_handler(lambda msg: msg.text == "💳 خرید اشتراک")
async def show_plans(message: types.Message):
    await message.answer("لطفا یکی از پلن‌ها را انتخاب کنید 👇", reply_markup=plans_menu)

@dp.message_handler(lambda msg: "کاربره" in msg.text)
async def plan_selected(message: types.Message):
    plan = message.text
    price = plan.split("-")[1].strip()
    await message.answer(
        f"✅ پلن انتخابی: {plan}\n"
        f"💳 لطفاً مبلغ {price} تومان را به شماره کارت زیر واریز کنید:\n\n"
        f"💳 6277 6013 6877 6066\nبنام رضوانی\n\n"
        f"سپس عکس فیش واریزی را ارسال کنید تا سفارش شما بررسی شود."
    )

@dp.message_handler(lambda msg: msg.text == "🔙 بازگشت")
async def back_to_main(message: types.Message):
    await message.answer("بازگشت به منوی اصلی 👇", reply_markup=main_menu)

@dp.message_handler(lambda msg: msg.text == "📚 آموزش اتصال")
async def show_help(message: types.Message):
    await message.answer(
        "📘 آموزش اتصال:\n"
        "۱. برنامه v2ray یا NapsternetV را نصب کنید\n"
        "۲. کانفیگی که برایتان ارسال می‌شود را وارد کنید\n"
        "۳. اتصال را فعال کنید\n\n"
        "⚠️ هر سوالی داشتید با پشتیبانی تماس بگیرید: @Psycho_remix1"
    )

@dp.message_handler(lambda msg: msg.text == "🛠 پشتیبانی")
async def support(message: types.Message):
    await message.answer("🔧 برای پشتیبانی با این آیدی در تماس باشید:\n@Psycho_remix1")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def receive_receipt(message: types.Message):
    await message.forward(config.ADMIN_ID)
    await bot.send_message(
        config.ADMIN_ID,
        f"📥 فیش جدید از طرف @{message.from_user.username or message.from_user.full_name}\n"
        f"آیدی عددی: {message.from_user.id}"
    )
    await message.answer("✅ فیش شما دریافت شد و در حال بررسی است.\nپس از تأیید، کانفیگ برای شما ارسال خواهد شد.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
