from pyrogram import Client, filters, idle
from pyrogram.types import *
from pymongo import MongoClient
from pyrogram import enums
import requests
import random
import os
import re

import Espro 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions


API_ID = os.environ.get("API_ID", "none") 
API_HASH = os.environ.get("API_HASH", "none") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "none") 
MONGO_URL = os.environ.get("MONGO_URL", "none")
BOT_IMAGE = os.environ.get("BOT_IMAGE", "none")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "none")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "none")
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "none")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "none")


bot = Client(
    "EsproChatBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.get_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐢 \n\n 𝐈'𝐦 𝐀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷.\n\n📌 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 𝐙𝐨𝐲𝐚 𝐅𝐨𝐫𝐦 𝐈𝐧𝐝𝐢𝐚 🇮🇳 \n\n🌷 𝐈'𝐦 𝐀 𝐀𝐫𝐭𝐢𝐟𝐢𝐜𝐢𝐚𝐥 𝐈𝐧𝐭𝐞𝐥𝐥𝐢𝐠𝐞𝐧𝐜𝐞 🌷\n\n /chatbot - [on|off] 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐔𝐬𝐞 𝐎𝐧𝐥𝐲 \n 𝐀𝐧𝐲 𝐆𝐫𝐨𝐮𝐩 💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » \n 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐂𝐡𝐚𝐭.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐌𝐞 𝐁𝐚𝐛𝐲", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "🍁𝐂𝐡𝐚𝐧𝐧𝐞𝐥🥀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                    InlineKeyboardButton(
                        "🍁𝐆𝐫𝐨𝐮𝐩🥀", url=f"https://t.me/{SUPPORT_GROUP}")
                ],
                [
                    InlineKeyboardButton(
                        "❄️𝐎𝐰𝐧𝐞𝐫❄️", url=f"https://t.me/{OWNER_USERNAME}")
                ]
           ]
        ),
    )
    
    
@bot.on_message(filters.command(["/start", f"start@{BOT_USERNAME}", "/ritik", ".himanshu", "#ritikraj", "#ritik"]) & filters.group)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""💥 𝐇𝐢! 𝐈'𝐦 𝐀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷.\n\n📌 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 𝐙𝐨𝐲𝐚 𝐁𝐨𝐭 🌷 𝐅𝐨𝐫𝐦 𝐈𝐧𝐝𝐢𝐚 🇮🇳 \n\n🌷 𝐈'𝐦 𝐀 𝐀𝐫𝐭𝐢𝐟𝐢𝐜𝐢𝐚𝐥 𝐈𝐧𝐭𝐞𝐥𝐥𝐢𝐠𝐞𝐧𝐜𝐞 🌷\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷\n\n /chatbot - [on|off]""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )



@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "💥 𝐇𝐞𝐲 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀 𝐀𝐝𝐦𝐢𝐧 💥"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:
        v.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"🌷 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🥀!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        await message.reply_text(f"🌷𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🥀!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:           
        await message.reply_text(f"💥 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲𝐄𝐧𝐚𝐛𝐥𝐞𝐝🌷!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        v.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"💥 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 🌷!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**🇮🇳 𝐔𝐬𝐚𝐠𝐞 🌷 :**\n/chatbot [on|off] 𝐎𝐧𝐥𝐲 𝐆𝐫𝐨𝐮𝐩 🇮🇳 !\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                   
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.botend(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.botend(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                    
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.botend(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       




spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🤗🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝐊𝐡𝐚𝐧𝐚 𝐊𝐡𝐚 𝐋𝐢𝐲𝐞 𝐉𝐢..??🥲** ",
           " **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " **𝐎𝐲𝐞 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐊𝐞𝐬𝐚 𝐇𝐚𝐢..??🤨** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞..??🙂** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **𝐒𝐨𝐧𝐚𝐥𝐢 𝐊𝐨𝐧 𝐇𝐚𝐢...??😅** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " **𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
           " **𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ 🄷ⒶᎥᏇ𝐀ຖ Ꮗ🄾ⱤᏝ𝐃 ](https://t.me/HaiwanWorld) 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐊𝐚𝐫 𝐋𝐨 𝐃𝐨𝐬𝐭 :- [⭕ ⏤‌⛦⃕‌❤🐉‌⃪‌ ᷟ⋆⃞⃪⃜🇷𝐢𝐭𝐢𝐤 🇷𝐚𝐣⍣⃪‌{™}─‌⃜⃜ 🔵](https://t.me/i_ii_ritikraj_ii_i) 🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [⭕ ⏤‌⛦⃕‌❤🐉‌⃪‌ ᷟ⋆⃞⃪⃜🇷𝐢𝐭𝐢𝐤 🇷𝐚𝐣⍣⃪‌{™}─‌⃜⃜ 🔵](https://t.me/i_ii_ritikraj_ii_i)🥰** ",
           " **𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
           ]

@bot.on_message(filters.command(["tagall", "spam", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.botend(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@bot.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")

bot.start()
print("Please 🥺 Haiwan Ko aapne Gf De Do")
idle()
