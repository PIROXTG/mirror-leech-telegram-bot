# REQUIRED CONFIG
BOT_TOKEN = ""
OWNER_ID = 0
TELEGRAM_API = 0
TELEGRAM_HASH = ""
# OPTIONAL CONFIG
TG_PROXY = {}
USER_SESSION_STRING = ""
CMD_SUFFIX = ""
AUTHORIZED_CHATS = "-1003223751108"
SUDO_USERS = ""
DATABASE_URL = ""
DATABASE_NAME = "mltbmltb"
STATUS_LIMIT = 4
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 15
FILELION_API = ""
STREAMWISH_API = ""
ALLDEBRID_API_KEY = ""
BUZZHEAVIER_ACCOUNT_ID = ""
BUZZHEAVIER_FOLDER_ID = ""
GOFILE_API_KEY = ""
TLDV_TOKEN = ""
EXCLUDED_EXTENSIONS = "aria2 !qB aria2 !qb html jpg png js txt srt nfo webp m4a exe iso rar zip inf mp3 pdf url png nfo tiff dat bundle hash json xml bin ini dll config torrent"
INCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
GALLERY_DL_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SUBSTITUTE = r"www\.[^\s]+ -  | Pahe\.(ink|ph|in|li)/PAHE/s | \[?YTS\.\w+ - YTS\.\w+\]?/YTS/s | YTS\.(MX|LT|BZ|GG|AM)/YTS/s | \]\[/  | [\(\)\[\]] | mkvCinemas|www\.SSRmovies\.Com|CineVood|Toonworld4all|[-.]HDHub4u\.Ms|MkvDrama\.Org|EZTVx\.to | [-.]?(www\.)?ExtraFlix\.pw//s | \.{2,}/. | ^[\s-]+ | \s+-\s*(\.\w{2,4})$/\1"
FFMPEG_CMDS = {"merge": ["-f concat -safe 0 -i mltb.txt -c copy mltb.mp4 -del"]}
UPLOAD_PATHS = {}
# GDrive Tools
GDRIVE_ID = ""
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""
# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""
# JDownloader
JD_EMAIL = ""
JD_PASS = ""
# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    }
]
# Nzb search
HYDRA_IP = ""
HYDRA_API_KEY = ""
# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "master"
# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = True
EQUAL_SPLITS = False
MEDIA_GROUP = False
USER_TRANSMISSION = False
HYBRID_LEECH = False
LEECH_FILENAME_PREFIX = ""
LEECH_DUMP_CHAT = "-1002076010933"
CLONE_DUMP_CHATS = ""
THUMBNAIL_LAYOUT = ""
FILES_LINKS = False
# qBittorrent/Aria2c
TORRENT_TIMEOUT = 3600
BASE_URL = ""
BASE_URL_PORT = 0
WEB_PINCODE = False
# Queueing system
QUEUE_ALL = 30
QUEUE_DOWNLOAD = 29
QUEUE_UPLOAD = 1
# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0
# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]
