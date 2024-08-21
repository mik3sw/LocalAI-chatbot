from util.decorator import restricted
from util.common import get_system_info
from telegram.constants import ParseMode

@restricted
async def func(update, context):
    msg = get_system_info()
    await context.bot.send_message(chat_id=update.message.chat_id,
                             text=msg,
                             parse_mode=ParseMode.HTML, disable_web_page_preview=True)