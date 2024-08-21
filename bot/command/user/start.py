from telegram.constants import ParseMode


async def func(update, context):
    """
    'start' provides the start message

    :param update: bot update
    :param context: CallbackContext
    :return: None
    """
    msg = "Chatbot ready! If this is the first time you use this bot, run the /init command"


    await context.bot.send_message(chat_id=update.message.chat_id,
                             text=msg,
                             parse_mode=ParseMode.HTML, disable_web_page_preview=True)