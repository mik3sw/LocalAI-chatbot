from util.decorator import restricted
from util.common import delete_user_interactions
from telegram.constants import ParseMode

@restricted
async def func(update, context):
    delete_user_interactions(update.message.from_user.id)

    # IF YOU DON'T WANT THE GIF COMMENT THIS PART AND UNCOMMENT THE SEND MESSAGE
    await context.bot.send_video(update.message.chat_id,
                            #  reply_to_message_id=update.message.message_id,
                             video='./images/giphy.gif.mp4',
                             caption="✅ <b>New chat started</b>",
                             parse_mode=ParseMode.HTML)
    
    #msg = "✅ New chat started"
    # await context.bot.send_message(chat_id=update.message.chat_id,
    #                          text=msg,
    #                          parse_mode=ParseMode.HTML, disable_web_page_preview=True)