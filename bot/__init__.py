####
##
#
#

from db.logger import logger

from ._bot import telebot as bot
from ._bot import *

from .utils import (
    process_pure_updates,
    process_updates,
    send_antiflood,
    set_webhook,
)

# isort:skip_file
from .command import command_ping_private

from .command import command_start_restart_private

from .command import echo_message


# from .command import (
#     chat_member_came_left,
#     command_ping_private,
#     command_say_private,
#     command_start_restart_private,
# )

# from autoload import autoload
#
# __all__ = autoload("command", "echo*")
# __all__ = autoload("command", "command*")
