import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to CobaloHub!\n\n"
        "Safe videos দেখতে /videos লিখুন."
    )

async def videos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Video List\n\n"
        "▶ Episode 1\n"
        "▶ Episode 2\n"
        "▶ Episode 3"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("videos", videos))

app.run_polling()
