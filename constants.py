import os

import sys

TOKEN = "SECRET_TOKEN"

HELP = """\
Puedes usar los siguientes comandos:
/help - muestra esta información.
/info - muesta información de interés.
/hello - saluda al bot.
/ping <ip o direccion> - hace ping a una direccion determinada. Por defecto www.google.es
"""

INFO = "Esta es la información."
HELLO = "Hola, soy GremioInformaticosBot, ¿qué tal?"
TYPING = "typing"
PING = "pong"
ACTUAL_OS_NAME = os.name
ACTUAL_PLATFORM_NAME = sys.platform
WINDOWS_OS_NAME = "nt"
LINUX_MAC_OS_NAME = "posix"
LINUX_PLATFORM = "linux2"
MAC_PLATFORM = "darwin"

DEFAULT_PING_DIRECTION = "www.google.es"
EXPECTED_PING_PARAMETERS = 2
PING_SUCCESS = 0
BAD_SERVER_MESSAGE = "Server {} unavailable."

LINUX_PING_COMMAND = "ping -c 3 {}"
WINDOWS_PING_COMMAND = "ping {}"
WINDOWS_OMIT_LINES = 1
LINUX_OMIT_LINES = 4

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
