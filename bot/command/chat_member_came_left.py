####
##
#
#

from bot import bot
from bot import logger as log
from bot import send_antiflood, types
from bot.options import PHRASE_FAREWELL, PHRASE_WELCOME
from settings import CRLF, TG_PARSE_MODE

# @bot.message_handler(
#     content_types=["new_chat_members", "left_chat_member"]
#     # chat_types=["private", "public", "group", "supergroup", "channel"],  # private у закрытых групп
# )
# content_type может быть одним из следующих строк:
# text, audio, document, photo, sticker, video, video_note, voice, location, contact,
# new_chat_members, left_chat_member, new_chat_title,
# new_chat_photo, delete_chat_photo,
# group_chat_created, supergroup_chat_created, channel_chat_created,
# migrate_to_chat_id, migrate_from_chat_id, pinned_message.


# new_chat_members event doesn't appear in channels. it's for group/supergroup only.
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_chat_members(message: types.Update):
    print("new_chat_member", message.chat.id, message.message_id, message.text)
    log.info("new mmbr chat {}".format(message))

    for chat_member in message.new_chat_members:
        # bot.edit_message_text(
        #    chat_id=message.chat.id,
        #    text=PHRASE_WELCOME.format(
        #        **{
        #            "prefix": "В чат заходит",
        #            "usertype": "коллега" if not chat_member.is_bot else "бот",
        #            "username": chat_member.username,
        #            "user_id": chat_member.id,
        #            "nickname": chat_member.full_name.strip() or chat_member.username,
        #            "suffix": (
        #                f"{CRLF}Спасибо, коллега\!" if not chat_member.is_bot else ""
        #            ),
        #        }
        #    ),
        # )

        # send_antiflood(
        bot.send_message(
            chat_id=message.chat.id,
            text=PHRASE_WELCOME.format(
                **{
                    "prefix": "В чат заходит",
                    "usertype": "коллега" if not chat_member.is_bot else "бот",
                    "username": chat_member.username,
                    "user_id": chat_member.id,
                    "nickname": (
                        chat_member.full_name.strip()
                        or chat_member.username
                        or "Anonymous"
                    ),
                    "suffix": (
                        f"{CRLF}Спасибо, коллега\!" if not chat_member.is_bot else ""
                    ),
                }
            ),
            # parse_mode="MarkdownV2",
        )

        bot.delete_message(message.chat.id, message.message_id)
    return


@bot.message_handler(content_types=["left_chat_member"])
def handler_left_chat_member(message: types.Update):
    print("left_chat_member", message.chat.id, message.message_id, message.text)
    chat_member = message.left_chat_member
    bot.delete_message(message.chat.id, message.message_id)
    send_antiflood(
        chat_id=message.chat.id,
        text=PHRASE_FAREWELL.format(
            **{
                "prefix": "Чат покидает",
                "usertype": "коллега" if not chat_member.is_bot else "бот",
                "username": chat_member.username,
                "user_id": chat_member.id,
                "nickname": (
                    chat_member.full_name.strip() or chat_member.username or "Anonymous"
                ),
                "suffix": "",
            }
        ),
    )
    return
