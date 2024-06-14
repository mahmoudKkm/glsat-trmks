from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""✪¦ اهلا بـك عزيـزي  {msg.from_user.mention}
✪¦ فـي بـوت اسـتـخـراج الـجـلـسـات
✪¦ يمكنك استخراج الجلسات الـتالية
✪¦ بايروجرام للحسابات & بايروجرام للبوتات
✪¦ بـايـروجـرام مـيوزك احـدث إصـدار 
✪¦ تيرمـكـس للحسابات & تيرمـكـس للبوتات

✪¦ بواسطـة : [𓊆سِٰــف‌ِٰــيِٰــر 𓊇 ⌁ 🕷](tg://user?id=7423117691) √""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⦓ بـدء اسـتـخـࢪاج جـلـسـة ⦔", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝚂𝙾𝚄𝚁𝚂 ⓢⓐⓕⓘⓡ 𓁓", url="https://t.me/M_T_lI"),
                    InlineKeyboardButton("ᯓ 𝙳𝙴𝚅 ⓢⓐⓕⓘⓡ ❥", user_id=7423117691)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
