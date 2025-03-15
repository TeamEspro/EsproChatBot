import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from EsproChat import EsproChat as app

LOGGER = getLogger(__name__)

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(500, 500)):
    """ Convert Image to Circular Format """
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")  # Fixed Pillow error
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)  # Fixed Pillow error
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):
    """ Generate Welcome Image """
    background = Image.open("EsproChat/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((825, 824))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('EsproChat/assets/font.ttf', size=110)
    draw.text((2100, 1420), f'ID: {id}', fill=(12000, 12000, 12000), font=font)
    pfp_position = (1990, 435)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"

@EsproChat.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    """ Welcome New Members with Image """
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await EsproChat.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "EsproChat/assets/upic.png"

    if temp.MELCOW.get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)

    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await EsproChat.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=f"""
**Wᴇʟᴄᴏᴍᴇ Tᴏ {member.chat.title}
➖➖➖➖➖➖➖➖➖➖➖➖
Nᴀᴍᴇ ✧ {user.mention}
Iᴅ ✧ {user.id}
Usᴇʀɴᴀᴍᴇ ✧ @{user.username}
➖➖➖➖➖➖➖➖➖➖➖➖**
""",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/MissEsproBot?startgroup=true")]])
        )
    except Exception as e:
        LOGGER.error(e)

    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass

@EsproChat.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    """ Notify When Bot Joins a New Group """
    for u in message.new_chat_members:
        if u.id == EsproChat.me.id:
            await EsproChat.send_message(LOG_CHANNEL_ID, f"""
**NEW GROUP
➖➖➖➖➖➖➖➖➖➖➖➖
NAME: {message.chat.title}
ID: {message.chat.id}
USERNAME: @{message.chat.username}
➖➖➖➖➖➖➖➖➖➖➖➖**
""")
