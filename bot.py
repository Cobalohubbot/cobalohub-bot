import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get("PORT", 10000))
URL = os.environ["RENDER_EXTERNAL_URL"]

app = Flask(__name__)

@app.route("/")
def home():
    return "CobaloHub Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to CobaloHub!\n\n"
        "📤 একটি ভিডিও পাঠাও।\n"
        "📺 /videos লিখে ভিডিও দেখো।"
    )

async def save_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Video received!")

async def videos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Video list coming soon!")

bot = Application.builder().token(TOKEN).build()

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CommandHandler("videos", videos))
bot.add_handler(MessageHandler(filters.VIDEO, save_video))

def run_web():
    app.run(host="0.0.0.0", port=PORT)

Thread(target=run_web).start()

bot.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=URL + "/telegram"
)
