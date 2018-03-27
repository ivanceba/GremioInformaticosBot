# -*- encoding: utf-8 -*-
import telebot
import time

from datetime import datetime

from constants import *


def make_readable(text: str) -> str:
    """
    Returns a readable string from a text

    :param text: text to convert
    :return: a readable text
    """
    out = ""

    for line in text:
        out += str(line) \
                   .replace("\\xa1", "í") \
                   .replace("\\xa0", "á") \
                   .replace("b'", "") \
                   .replace("\\r", "") \
                   .replace("\\n", "") \
                   .replace("'", "") + '\n'

    return out


class GremioInformaticosBot:
    """
    This is a class that starts a bot.
    """

    def __init__(self):
        """
        Initializes a bot.
        """
        self.bot = telebot.TeleBot(TOKEN)

        def __listener(*args) -> None:
            """
            Listener that has log all the messages

            :param args: message(s)
            :return: None
            """
            message = None

            for m in args:
                chat = m.pop(0)
                cid = chat.chat.id
                if cid > 0:
                    message = "{}: {} []: {}" \
                        .format(datetime.now().strftime(DATE_FORMAT), chat.chat.first_name, {cid}, chat.text)
                else:
                    message = "{}: {} [{}]@({}): {}" \
                        .format(datetime.now().strftime(DATE_FORMAT), chat.from_user.first_name,
                                cid, chat.chat.title, chat.text)
                f = open('log.txt', 'a')
                try:
                    f.write(message + '\n')
                except Exception:
                    f.write("Message error from {}\n".format(cid))
                f.close()

            print(message)

        self.listener = __listener

        @self.bot.message_handler(commands=['help', 'ayuda'])
        def help_command(m):
            cid = m.chat.id

            self.bot.send_chat_action(cid, TYPING)
            time.sleep(1)
            self.bot.send_message(cid, HELP)

        @self.bot.message_handler(commands=['info'])
        def info_command(m):
            cid = m.chat.id
            self.bot.send_chat_action(cid, TYPING)
            time.sleep(1)
            self.bot.send_message(cid, INFO)

        @self.bot.message_handler(commands=['hello', 'hola'])
        def hello_command(m):
            cid = m.chat.id
            self.bot.send_chat_action(cid, TYPING)
            time.sleep(1)
            self.bot.send_message(cid, HELLO)

        @self.bot.message_handler(commands=["ping"])
        def ping_command(m):
            cid = m.chat.id

            direction = DEFAULT_PING_DIRECTION if len(m.text.split()) < EXPECTED_PING_PARAMETERS \
                else m.text.split()[EXPECTED_PING_PARAMETERS - 1]

            result = os.system((WINDOWS_PING_COMMAND if ACTUAL_OS_NAME == WINDOWS_OS_NAME else LINUX_PING_COMMAND)
                               .format(direction))

            if result is not PING_SUCCESS:
                self.bot.send_message(cid, BAD_SERVER_MESSAGE.format(direction))
                return

            import subprocess
            ping = subprocess.Popen(
                    (['ping', direction]
                     if ACTUAL_OS_NAME == WINDOWS_OS_NAME
                     else ['ping', '-c 3', direction]),
                    stdout=subprocess.PIPE
            )

            for i in range(LINUX_OMIT_LINES if ACTUAL_OS_NAME == LINUX_MAC_OS_NAME else WINDOWS_OMIT_LINES):
                ping.stdout.readline()

            self.bot.send_chat_action(cid, TYPING)
            self.bot.send_message(cid, make_readable(ping.stdout.readlines()))

        @self.bot.message_handler(func=lambda message: message.text.lower() == "hola")
        def command_text_hello(m):
            self.bot.send_chat_action(m.chat.id, TYPING)
            time.sleep(1)
            self.bot.send_message(m.chat.id, "Hola a ti también.")

    def __str__(self):
        return self.__name__ + " running."

    def start(self):
        print("Bot is ready.")
        self.bot.set_update_listener(self.listener)
        self.bot.polling()
