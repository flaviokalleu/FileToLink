import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '22594796'))
API_HASH = environ.get('API_HASH', 'ef1f82927273518ebb576665d7c63a55')
BOT_TOKEN = environ.get('BOT_TOKEN', "7409134871:AAHyhIJKnIs3Xmi-CnlSDUR8cmYOiJPvsfs")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "thebestpromotionoftday.com")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002496388570'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1404280160').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb://newtelegram:crMyESTfFhhrwrAR@142.44.199.238:27017/newtelegram")
DATABASE_NAME = environ.get('DATABASE_NAME', "newtelegram")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', True)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'hRPS5vvZc0OGOEUQJMJzPiojoVK2')
