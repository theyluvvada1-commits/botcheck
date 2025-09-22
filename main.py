import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is alive and token works!")

def main():
    if not TOKEN:
        print("❌ No token found. Did you set TELEGRAM_BOT_TOKEN in Render?")
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot starting... go to Telegram and type /start")
    app.run_polling()

if __name__ == "__main__":
    main()
