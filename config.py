import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "29650844")) #optional
API_HASH = getenv("API_HASH", "6154d581d370cbdadd240292c456d7a2") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8187361583 1281282633").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/9ee37cccd7bf55c3ec953.png')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/HeartBeat_Muzic")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQHEb5wAjh-VJhJTbGAt_16pIrZF4l6cjP-QxNGnnWSaWCZK7VXM4CeOa-7tvG2zawSFwjJ7j-2RgUSRQFMVNQG1MClEtmKV7gdGGiLliJLyQdAbclUPdpkqSWtyiQHrpekPh98VVCOPR97aryTuNZ1fDfIb5_fq0Ik1HTJNV3pv-YMpL2bcpM6r24rDmu_9v9L1wSkaZAQfXTPFNLZuuOspTwWFf-SWu15jYNn8KGohQOalyPkIDWCozJYarP4gwokvEb4EM55nP7GgeQFmc9YymT0hGoDQfNF91g-AOmCWTSqp2o9rU5EojNImgDc91TbCHS8u7k7TvHixm_JJF2NXzzf6RwAAAAHHZ9BxAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
