# import modules
import command
from telegram.ext import CommandHandler


def admin_command(application):
    application.add_handler(CommandHandler(["new", "newchat"], command.admin.new.func))
    application.add_handler(CommandHandler("init", command.admin.init.func))
    application.add_handler(CommandHandler("status", command.admin.status.func))

def user_command(application):
    application.add_handler(CommandHandler("help", command.user.help.func))
    application.add_handler(CommandHandler("start", command.user.start.func))