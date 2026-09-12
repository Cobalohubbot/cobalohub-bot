import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["BOT_TOKEN"]

# Bot চালু থাকা অবস্থায় ভিডিওগুলো এখানে থাকবে
videos = []


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to CobaloHub!\n\n"
        "📤 আমাকে একটি ভিডিও পাঠাও।\n"
        "📺 /videos লিখলে ভিডিওগুলো দেখতে পারবে।"
    )


async def save_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video

    videos.append(video.file_id)

    number = len(videos)

    await update.message.reply_text(
        f"✅ Video {number} saved!\n\n"
        f"📺 দেখতে /videos লিখুন।"
    )


async def show_videos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not videos:
        await update.message.reply_text(
            "📭 এখনো কোনো ভিডিও যোগ করা হয়নি।"
        )
        return

    await update.message.reply_text(
        f"🎬 CobaloHub Video List\n\n"
        f"মোট ভিডিও: {len(videos)}"
    )

    for i, file_id in enumerate(videos, start=1):
        await update.message.reply_video(
            video=file_id,
            caption=f"🎬 Video {i}"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("videos", show_videos))

app.add_handler(
    MessageHandler(filters.VIDEO, save_video)
)

PORT = int(os.environ.get("PORT", 10000))
WEBHOOK_URL = os.environ.get("RENDER_EXTERNAL_URL")

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL
)
