from nonebot.rule import Rule
from nonebot.adapters import Event


async def isMediaContent(event:Event) -> bool:
    message = event.get_message()
    if message.has("image") or message.has("video") or message.has("file"):
        return True
    elif message.has("forward"):
        return True
    else:
        return False
    