from telegram.constants import ParseMode
from telegram import ChatPermissions
from telegram.error import Forbidden
from configparser import ConfigParser
import logging
from util.decorator import restricted
from util.model import generate_answer

# setup logger
logger = logging.getLogger(__name__)

@restricted
async def chat(update, context):
    """
    Chat messages
    """

    prompt = update.message.text
    user_id = update.message.from_user.id

    msg = generate_answer(prompt, user_id)
    await context.bot.send_message(chat_id=update.message.chat_id,
                             text=msg,
                             parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


# trigger all functions defined above
async def init(update, context):
    await chat(update, context)