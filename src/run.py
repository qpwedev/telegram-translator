"""
Contains the main logic for the translation bot.
"""

import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from googletrans import Translator
from validator import validate_env_variables
from art import text2art

load_dotenv()

print(text2art("TTranslator", font="small"))

translator = Translator()

validate_env_variables()


API_ID, API_HASH, FIRST_LANGUAGE, SECOND_LANGUAGE = (
    os.getenv("API_ID"),
    os.getenv("API_HASH"),
    os.getenv("FIRST_LANGUAGE"),
    os.getenv("SECOND_LANGUAGE"),
)


app = Client("my_account", int(API_ID), API_HASH)


def detect_language(text: str) -> str:
    """
    Detects the language of the given text.

    Parameters:
    - text: The text for which to detect the language.

    Returns:
    - A string representing the detected language code (e.g., 'en' for English).
    """
    detected = translator.detect(text)
    return detected.lang


# More about filters at https://docs.pyrogram.org/topics/use-filters
@app.on_message(filters.me & (filters.text))
async def message_handler(_, message: Message):
    """
    Catch all messages from the user and translate them to English
    """

    detected_language = translator.detect(message.text).lang

    if detected_language == FIRST_LANGUAGE:
        target_language = SECOND_LANGUAGE
    elif detected_language == SECOND_LANGUAGE:
        target_language = FIRST_LANGUAGE
    else:
        return

    translated_message_text = translator.translate(
        message.text, src=detected_language, dest=target_language
    ).text

    if message.text == translated_message_text:
        return

    await message.edit(
        f"{message.text}\n\n-auto translation-\n\n{translated_message_text}"
    )


if __name__ == "__main__":
    app.run()
