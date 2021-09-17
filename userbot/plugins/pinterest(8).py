#Created by @MineisZarox
from urllib import request
from userbot import catub
import re
import requests
from ..core.managers import edit_delete, edit_or_reply
import os
try:
    from pyquery import PyQuery as pq
except ModuleNotFoundError:
    os.system("pip3 install pyquery")
    from pyquery import PyQuery as pq

plugin_category = "extra"

def get_download_url(link):
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = pq(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')
    return download_url

@catub.cat_cmd(
    pattern="pinterest?(?:\s|$)([\s\S]*)",
    command=("pinterest", plugin_category),
    info={
        "header": "To download pinterest posts",
        "options": "To download image and video posts from pinterest",
        "usage": [
            "{tr}pinterest <post link>",
        ],
    },
)
async def _(event):
    "To download pinterest posts"
    A = event.pattern_match.group(1)
    links = re.findall(r"\bhttps?://.*\.\S+", A)
    await event.delete()
    if not links:
        L = await event.respond("`Please give a valid link`")
        await asyncio.sleep(2)
        await L.delete()
    else:
        pass
    K = await event.respond("`Downloading...`")
    MINE = get_download_url(A)
    await event.client.send_file(event.chat.id, MINE)
    await K.delete()
