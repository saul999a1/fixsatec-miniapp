from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")  # Asegúrate de configurar esta variable en Railway o donde lo alojes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Abrir Mini App", web_app={"url": "https://saul999a1.github.io/fixsatec-miniapp/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 ¡Bienvenido a FixSaTec!\n\nUsa el botón para abrir la Mini App o escribe /menu para ver los comandos.",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Comandos disponibles:\n"
        "/start - Mostrar mensaje de bienvenida\n"
        "/menu - Mostrar este menú\n"
        "/soporte - Contactar a un técnico\n"
        "/info - Información sobre la app"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ FixSaTec es una app para ayudarte con diagnósticos y soporte técnico.")

async def soporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔧 Un técnico se pondrá en contacto contigo pronto.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("soporte", soporte))

app.run_polling()
