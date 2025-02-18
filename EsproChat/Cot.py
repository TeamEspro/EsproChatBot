
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from PIL import Image, ImageDraw, ImageFont, ImageChops

# Logging Setup
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Bot Token and API Credentials (Replace with your own)
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Paths to Assets
DEFAULT_BG = "assets/welcome_bg.png"  # Custom background image
DEFAULT_PFP = "assets/default_pfp.png"  # Default profile picture
FONT_PATH = "assets/font.ttf"  # Font for writing text

# Initialize Bot
app = Client("welcome_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def circle(pfp, size=(300, 300)):
    """Convert profile picture into a circular image."""
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    pfp.putalpha(mask)
    return pfp

def create_welcome_image(pfp_path, user_name, user_id, username, chat_title):
    """Create a welcome image with user's details."""
    try:
        bg = Image.open(DEFAULT_BG).convert("RGBA")
        pfp = Image.open(pfp_path).convert("RGBA") if os.path.exists(pfp_path) else Image.open(DEFAULT_PFP).convert("RGBA")
        pfp = circle(pfp)

        # Paste Profile Picture
        bg.paste(pfp, (80, 80), pfp)

        # Draw Text
        draw = ImageDraw.Draw(bg)
        font_large = ImageFont.truetype(FONT_PATH, 50)
        font_small = ImageFont.truetype(FONT_PATH, 35)

        draw.text((420, 120), f"Welcome to {chat_title}!", (255, 255, 255), font=font_large)
        draw.text((420, 200), f"👤 Name: {user_name}", (255, 255, 255), font=font_small)
        draw.text((420, 250), f"🔗 Username: {username}", (255, 255, 255), font=font_small)
        draw.text((420, 300), f"🆔 User ID: {user_id}", (255, 255, 255), font=font_small)

        # Save Image
        output_path = f"downloads/welcome_{user_id}.png"
        bg.save(output_path)
        return output_path
    except Exception as e:
        LOGGER.error(f"Error creating welcome image: {e}")
        return None

@app.on_chat_member_updated(filters.group)
async def welcome_message(_, member: ChatMemberUpdated):
    """Send a welcome message with an image when a new user joins."""
    if (
        member.new_chat_member
        and member.new_chat_member.status == "member"  # Ensure user just joined
    ):
        chat_id = member.chat.id
        user = member.new_chat_member.user
        first_name = user.first_name or "Unknown"
        username = f"@{user.username}" if user.username else "No Username"
        user_id = user.id

        # Download Profile Picture
        pic_path = f"downloads/pp_{user_id}.png"
        try:
            pfp = await app.download_media(user.photo.big_file_id, file_name=pic_path)
        except AttributeError:
            pfp = DEFAULT_PFP  # Use default profile pic if no photo exists

        # Generate Welcome Image
        welcome_img = create_welcome_image(pfp, first_name, user_id, username, member.chat.title)
        if welcome_img:
            await app.send_photo(chat_id, photo=welcome_img, caption=f"👋 Welcome, {first_name}!\n🆔 `{user_id}`\n🔗 {username}")
        
        # Cleanup
        try:
            os.remove(welcome_img)
            os.remove(pic_path)
        except Exception:
            pass
