#By @FeelDeD
from userbot import catub
from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "useless"

@catub.cat_cmd(
    pattern="xgs ?(.*)",
    command=("xgs", plugin_category),
    info={
        "header": "Fun google animated sticker",
        "usage": [
            "{tr}xgs <your text>",
        ],
    },
)
async def app(odi):
    
    if odi.fwd_from:
        return
    bot = "@GooglaxBot "
    text = odi.pattern_match.group(1)
    reply_to_id = await reply_id(odi)
    if not text:
        return await edit_delete(odi, "`Give me some text, Lmao`")
    else:
    	    await odi.delete()
    	    run = await odi.client.inline_query(bot, text)
    	    result = await run[0].click("me")
    	    await result.delete()
    	    await odi.client.send_message(odi.chat_id, result, reply_to=reply_to_id)