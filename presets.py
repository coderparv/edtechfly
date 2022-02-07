class Presets(object):
    WELCOME_MESSAGE = *Hello 
I'm an anime-theme management bot [✨](https://telegra.ph/file/11b5922a33de9968cedfe.jpg)
────────────────────────
 

buttons = [
    [
        InlineKeyboardButton(text="About Emiko Robot", callback_data="emiko_"),
    ],
    [
        InlineKeyboardButton(text="Get Help", callback_data="help_back"),
        InlineKeyboardButton(
            text="Try inline!​​", switch_inline_query_current_chat=""
        ),
    ],
    [
        InlineKeyboardButton(
            text="➗ Add Emiko To Your Group ➗", url="t.me/EmiexRobot?startgroup=new"),
    ],
]

    USERS_LIST = "<b>Total:</b>\n\nSubscribers - {}\nBlocked / Deleted - {}"
    WAIT_MSG = "<b>Please Wait...</b>"
    REPLY_ERROR = "<code>Use this command as a reply to any telegram message with out any spaces.</code>"
