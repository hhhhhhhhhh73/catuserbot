#By @FeelDeD
import os
from PIL import Image, ImageEnhance
from userbot import catub
from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "useless"

@catub.cat_cmd(
    pattern="dark ?(.*)",
    command=("dark", plugin_category),
    info={
        "header": "Photo darkener",
        "description": "Reply to Image to dark it",
         "flags": {
            "d": "Dead mode",
        },
        "usage": [
            "{tr}dark <reply a pic>",
            "{tr}dark d <reply a pic>",
        ],
    },
)
async def dark(odi):
    "Darkener"
    if odi.fwd_from:
        return
    await odi.edit("`Processing ...`")
    mode = odi.pattern_match.group(1)
    if mode == "d": factor = 0.1
    else: factor = 0.5
    reply_to_id = await reply_id(odi)
    get = await odi.get_reply_message()
    if not get:
    	return await edit_delete(odi, "`Please reply a photo`", 5)
    if not get.photo:
    	return await edit_delete(odi, "`Please reply a photo`", 5)
    else:
    	dl = await odi.client.download_media(get)
    	img = Image.open(dl)
    	bw = img.convert('L')
    	enhancer = ImageEnhance.Brightness(bw)
    	output = enhancer.enhance(factor)
    	end = output.save("Dark.png")
    	await odi.client.send_file(odi.chat_id, file="Dark.png", reply_to=reply_to_id)
    	await odi.delete()
    	os.remove(dl)
    	os.remove("Dark.png")
