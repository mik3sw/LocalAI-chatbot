from telegram.constants import ParseMode


async def func(update, context):
    """
    'help' provides the help message

    :param update: bot update
    :param context: CallbackContext
    :return: None
    """
    msg = "MESSAGGIO HELP"

    await context.bot.send_message(chat_id=update.message.chat_id,
                             text=msg,
                             parse_mode=ParseMode.HTML, disable_web_page_preview=True)