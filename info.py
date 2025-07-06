# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '20517170'))
API_HASH = environ.get('API_HASH', 'f09e5c91dd864f01063ff63827832137')
BOT_TOKEN = environ.get('BOT_TOKEN', "7823999255:AAFDzngdBb48ebF2xgdbTXwAID3uYYAo5Ug")


# This Pictures Is For Start Message Picture, You Can Add Multiple By Giving One Space Between Each.
PICS = (environ.get('PICS', 'https://i.ibb.co/6cx2b4PC/Picsart-25-06-03-12-44-42-940.jpg')).split()


# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7640330255').split()] # For Multiple Id Use One Space Between Each.
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '7640330255').split()]  # For Multiple Id Use One Space Between Each.
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# This Channel Is For When User Start Your Bot Then Bot Send That User Name And Id In This Log Channel, Same For Group Also.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002634887109'))
DUMP_CHANNEL = int(os.environ.get('DUMP_CHANNEL', '-1002652418330'))
INSTA_CHANNEL = int(environ.get('INSTA_CHANNEL', '-1002668185724'))

# This Is File Channel Where You Upload Your File Then Bot Automatically Save It In Database 
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002874372912').split()]  # For Multiple Id Use One Space Between Each.

# auth_channel means force subscribe channel.
# if REQUEST_TO_JOIN_MODE is true then force subscribe work like request to join fsub, else if false then work like normal fsub.
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False)) # Set True Or False
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False)) # Set True Or False (This try again button is only for request to join fsub not for normal fsub)

# This Is Force Subscribe Channel, also known as Auth Channel 
auth_channel = environ.get('AUTH_CHANNEL', '-1002819734434') # give your force subscribe channel id here else leave it blank
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# This Channel Is For When User Request Any File Name With command or hashtag like - /request or #request
reqst_channel = environ.get('REQST_CHANNEL', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

# This Channel Is For Index Request 
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

# This Is Your Bot Support Group Id , Here Bot Will Not Give File Because This Is Support Group.
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# This Channel Is For /batch command file store.
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002603042037')).split()]  # For Multiple Id Use One Space Between Each.

# This Channel Is For Delete Index File, Forward Your File In This Channel Which You Want To Delete Then Bot Automatically Delete That File From Database.
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]  # For Multiple Id Use One Space Between Each.


# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vijayxbotz917:BHq1zCm83wVWhRUL@cluster0.lavhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   # IF Multiple Database Is False Then Fill Only This Database Url.
DATABASE_NAME = environ.get('DATABASE_NAME', "techvjclonefilterbot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'vjcollection')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False)) # Set True or False

# If Multiple Database Is True Then Fill All Three Below Database Uri Else You Will Get Error.
O_DB_URI = environ.get('O_DB_URI', "")   # This Db Is For Other Data Store
F_DB_URI = environ.get('F_DB_URI', "")   # This Db Is For File Data Store
S_DB_URI = environ.get('S_DB_URI', "")   # This Db is for File Data Store When First Db Is Going To Be Full.


# Premium And Referal Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month') # time in week, day, month.
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/ce1723991756e48c35aa1.jpg') # payment code picture url.
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 30ʀs - 1 ᴡᴇᴇᴋ\n- 50ʀs - 1 ᴍᴏɴᴛʜs\n- 120ʀs - 3 ᴍᴏɴᴛʜs\n- 220ʀs - 6 ᴍᴏɴᴛʜs\n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\n✨ ᴜᴘɪ ɪᴅ - <code>demo@okxyz</code>\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ</b>')


# Clone Information : If Clone Mode Is True Then Bot Clone Other Bots.
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "") # Necessary If clone mode is true
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '') # Public Channel Username Without @ or without https://t.me/ and Bot Is Admin With Full Right.


# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Msd_Movies_Request')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/MS_Movieszzz')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/MSD_Support_Group') # Support Chat Link Without https:// or @
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/iam_Vijay_Bot')

# True Or False
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
BUTTON_MODE = bool(environ.get('BUTTON_MODE', True))
MAX_BTN = bool(environ.get('MAX_BTN', True))
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
IMDB = bool(environ.get('IMDB', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))


# Token Verification Info :
VERIFY = bool(environ.get('VERIFY', False))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')

# If You Fill Second Shortner Then Bot Attach Both First And Second Shortner And Use It For Verify.
VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', False))
# if verify second shortner is True then fill below url and api
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')


# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', '') # How Open Shortner Link Video Link , Channel Link Where You Upload Your Video.


# Others
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', '𝐇ᴇʟʟᴏ 𝐌ʏ 𝐃ᴇᴀʀ 𝐅ʀɪᴇɴᴅꜱ ᥫ᭡')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)


# Choose Option Settings 
LANGUAGES = ["Tᴀᴍɪʟ", "Tᴀᴍ", "Tᴇʟᴜɢᴜ", "Tᴇʟ" ,"Mᴀʟᴀʏᴀʟᴀᴍ", "Mᴀʟ", "Kᴀɴɴᴀᴅᴀ", "Kᴀɴ", "Hɪɴᴅɪ", "Hɪɴ", "Eɴɢʟɪsʜ", "Eɴɢ"]
SEASONS = ["Sᴇᴀsᴏɴ 𝟶𝟷", "Sᴇᴀsᴏɴ 𝟶𝟸", "Sᴇᴀsᴏɴ 𝟶𝟹", "Sᴇᴀsᴏɴ 𝟶𝟺", "Sᴇᴀsᴏɴ 𝟶𝟻", "Sᴇᴀsᴏɴ 𝟶𝟼", "Sᴇᴀsᴏɴ 𝟶𝟽", "Sᴇᴀsᴏɴ 𝟶𝟾", "Sᴇᴀsᴏɴ 𝟶𝟿", "Sᴇᴀsᴏɴ 𝟷𝟶"]
EPISODES = ["E 𝟶𝟷", "E 𝟶𝟸", "E 𝟶𝟹", "E 𝟶𝟺", "E 𝟶𝟻", "E 𝟶𝟼", "E 𝟶𝟽", "E 𝟶𝟾", "E 𝟶𝟿", "E 𝟷𝟶", "E 𝟷𝟷", "E 𝟷𝟸", "E 𝟷𝟹", "E 𝟷𝟺", "E 𝟷𝟻", "E 𝟷𝟼", "E 𝟷𝟽", "E 𝟷𝟾", "E 𝟷𝟿", "E 𝟸𝟶", "E 𝟸𝟷", "E 𝟸𝟸", "E 𝟸𝟹", "E 𝟸𝟺", "E 𝟸𝟻", "E 𝟸𝟼", "E 𝟸𝟽", "E 𝟸𝟾", "E 𝟸𝟿", "E 𝟹𝟶", "E 𝟹𝟷", "E 𝟹𝟸", "E 𝟹𝟹", "E 𝟹𝟺", "E 𝟹𝟻", "E 𝟹𝟼", "E 𝟹𝟽", "E 𝟹𝟾", "E 𝟹𝟿", "E  𝟺𝟶"]
QUALITIES = ["𝟹𝟼𝟶 P", "𝟺𝟾𝟶 P", "𝟽𝟸𝟶 P", "𝟷𝟶𝟾𝟶 P", "𝟷𝟺𝟺𝟶 P", "𝟸𝟷𝟼𝟶 P"]
YEARS = ["𝟷𝟿𝟶𝟶", "𝟷𝟿𝟿𝟷", "𝟷𝟿𝟿𝟸", "𝟷𝟿𝟿𝟹", "𝟷𝟿𝟿𝟺", "𝟷𝟿𝟿𝟻", "𝟷𝟿𝟿𝟼", "𝟷𝟿𝟿𝟽", "𝟷𝟿𝟿𝟾", "𝟷𝟿𝟿𝟿", "𝟸𝟶𝟶𝟶", "𝟸𝟶𝟶𝟷", "𝟸𝟶𝟶𝟸", "𝟸𝟶𝟶𝟹", "𝟸𝟶𝟶𝟺", "𝟸𝟶𝟶𝟻", "𝟸𝟶𝟶𝟼", "𝟸𝟶𝟶𝟽", "𝟸𝟶𝟶𝟾", "𝟸𝟶𝟶𝟿", "𝟸𝟶𝟷𝟶", "𝟸𝟶𝟷𝟷", "𝟸𝟶𝟷𝟸", "𝟸𝟶𝟷𝟹", "𝟸𝟶𝟷𝟺", "𝟸𝟶𝟷𝟻", "𝟸𝟶𝟷𝟼", "𝟸𝟶𝟷𝟽", "𝟸𝟶𝟷𝟾", "𝟸𝟶𝟷𝟿", "𝟸𝟶𝟸𝟶", "𝟸𝟶𝟸𝟷", "𝟸𝟶𝟸𝟸", "𝟸𝟶𝟸𝟹", "𝟸𝟶𝟸𝟺", "𝟸𝟶𝟸𝟻"]


                           # Don't Remove Credit @VJ_Botz
                           # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
                           # Ask Doubt on telegram @KingVJ01


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://msdxfilter01-cce0c45d7c1a.herokuapp.com/")


# Rename Info : If True Then Bot Rename File Else Not
RENAME_MODE = bool(environ.get('RENAME_MODE', False)) # Set True or False


# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False)) # Set True or False


# Start Command Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions


if MULTIPLE_DATABASE == False:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI    # This Db is for User Data Store
    OTHER_DB_URI = O_DB_URI       # This Db Is For Other Data Store
    FILE_DB_URI = F_DB_URI        # This Db Is For File Data Store
    SEC_FILE_DB_URI = S_DB_URI    # This Db is for File Data Store When First Db Is Going To Be Full.


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
