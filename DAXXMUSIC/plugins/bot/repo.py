from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✧ ᴡᴀʟᴄᴏᴍᴇ ᴛᴏ ғʟᴇx ʙᴏᴛs ✧

text = f"<b>➲  : <a href='https://t.me/EMXES_COMMUNITY'>𝗘𝗠𝗫𝗘𝗦 𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬</a>\n➲ : <a href='https://t.me/FleX_Bots_News'>𝗙𝗟𝗘𝗫 𝗕𝗢𝗧𝗦 𝗨𝗣𝗗𝗔𝗧𝗘</a>\➲ : <a href='https://t.me/Flex_Support_Chat'>𝗙𝗟𝗘𝗫 𝗕𝗢𝗧 𝗦𝗨𝗣𝗣𝗢𝗥𝗧</a>\n➲ : <a href='https://t.me/EMXES_NETWORK'>𝗘𝗠𝗫𝗘𝗦 𝗡𝗘𝗧𝗪𝗢𝗥𝗞</a>\➲ : <a href='https://t.me/KAMUI_NETWORK'>𝗞𝗔𝗠𝗨𝗜 𝗡𝗘𝗧𝗪𝗢𝗥𝗞</a>\n➲ : <a href='https://t.me/The_Trader_Zone'>𝗪/𝗛 𝗧𝗥𝗔𝗗𝗘 𝗔𝗥𝗘𝗔</a></b>
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/HEROKUFREECC"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Qweibie"),
          ],
               [
                InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url="https://t.me/ALLTYPECC"),

],
[
              InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟︎", url=f"https://github.com/DAXXTEAM/DAXXBANALL"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/DAXXTEAM/DAXXMUSIC"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://github.com/DAXXTEAM/YumikooRobot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXCHATBOT"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXSTRINGBOT"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧𝗚𝗣𝗧", url=f"https://github.com/DAXXTEAM/DAXXCHATGPT"),
],
[
              InlineKeyboardButton("𝗩𝗣𝗦", url=f"https://github.com/DAXXTEAM/Kaali-Linux"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://github.com/DAXXTEAM/DAXXMOVIEBOT"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://github.com/DAXXTEAM/DAXXSTRINGHACK"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXIDCHAT"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXUSERBOT"),
InlineKeyboardButton("𝗦𝗘𝗔𝗥𝗖𝗛𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/SEARCH_BOT"),
],
[
InlineKeyboardButton("𝗖𝗖 𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/CC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/29f9791ee081bf1b5a9c2.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/DAXXTEAM/DAXXMUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/ANIME_IMMORTAL)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


