from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен должен быть в виде строки, обернутой в кавычки
TOKEN = '8196182322:AAHRxMorYrTouMpVizzm9hvY6a_-XYCxDaU'

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот. Пиши мне, если нужна помощь!")

# Основная функция запуска
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
