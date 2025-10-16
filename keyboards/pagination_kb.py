from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON

def create_pagination_keyboard(*buttons:str)->InlineKeyboardMarkup:

    kb_build = InlineKeyboardBuilder()

    kb_build.row(
        *[
            InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button,
            )
            for button in buttons
        ]
    )
    return kb_build.as_markup()
