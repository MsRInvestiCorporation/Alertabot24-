import os
from telegram.ext import Application, CommandHandler
from telegram.ext import ContextTypes

TOKEN = os.getenv("TOKEN")
CANAL_ID = "@MsRInvestCorporation"

async def start(update, context):
    await update.message.reply_text("👋 Olá, Messias! O bot está ativo e pronto para enviar alertas.")

async def enviar_alerta(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CANAL_ID,
        text="🚨 O Messias e a Mônica são brilhantes! 💡"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.job_queue.run_repeating(enviar_alerta, interval=60, first=0)
    app.run_polling()

if __name__ == "__main__":
    main()
