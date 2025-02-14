import os
import openai
from pymongo import MongoClient
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load environment variables
load_dotenv()

# Get API keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["telegram_bot"]
collection = db["chat_history"]

# Function to check if a message is already saved
def get_saved_response(user_message):
    data = collection.find_one({"message": user_message})
    return data["response"] if data else None

# Function to save new response in MongoDB
def save_response(user_id, username, user_message, bot_response):
    collection.insert_one({
        "user_id": user_id,
        "username": username,
        "message": user_message,
        "response": bot_response
    })

# Function to get response from OpenAI
def get_gpt_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        return response["choices"][0]["message"]["content"]
    except:
        return "Kuch gadbad ho gayi! Kripya baad me try karein."

# Start command function
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Main ek AI chatbot hoon. Aap mujhse private ya group chat me baat kar sakte hain.")

# Function to handle user messages
async def chat_with_bot(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username or "Unknown"
    user_message = update.message.text

    # Check if response is already saved
    saved_response = get_saved_response(user_message)

    if saved_response:
        bot_reply = saved_response
    else:
        bot_reply = get_gpt_response(user_message)
        save_response(user_id, username, user_message, bot_reply)

    await update.message.reply_text(bot_reply)

# Main function to run the bot
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_bot))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
