import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6403785146:AAFZrpcYWKHjsDIkGvFBZZYkxDgJcKi1ZeM")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "29310987"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "336c28913a45587a4c10af8cd620b68f")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6515901556").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "leo")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "BQG_QAsAOnnSf6WXa2wIDvXItZ6wxGueSCqBIaQWbh_nxOYZWG9Yf8d-U-j_oyDLtZnWYeHHKmmWl-j1IJNeAi12oYLKrnqrPCaH98I7kuRdReu4M2jV1G_joSHKnocEMRcFpBo8Dgs8yq6nFBOUc4tUgT7C5RUh2tWli1utTxNnwB-T6nCWunokT83PJD90feAXqtGQK31UuHuTfdGBh0LH7v98ZTW_jJoKw8ESxfpGtiv8w8SoKraaF5YXP-UifK95_Tp3F9ZoIYbYJ1b0LOWm9Mj6t7KsgjQ-C4yIlA9A0kIlmyky3vbplULhwC2cQapDt7t2QUsfqFk9zKanRnq0F2u54AAAAAGEYMR0AA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
