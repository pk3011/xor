from dotenv import load_dotenv
import os
from file_xor.lib.runtime_utils import load_host_url

# Load dotenv and override any existing environment variables so
# values in config.env (like LANG) take precedence over the system env.
load_dotenv("config.env", override=True)


class TgConfig:
    # Telegram related configurations
    API_ID = int(os.environ.get("API_ID", "1747265"))
    API_HASH = os.environ.get("API_HASH", "API_HASH=47f031293f55361c76c27da11916179b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8173103912:AAFus6z_SSJmg6C-X0WX99qTRD5j-p9eMMU")
    FILEDB_CHANNEL = int(os.environ.get("FILEDB_CHANNEL", "-1003348559182"))
   

class ServerConfig:
    # Server related configurations
    DOMAIN_URL = os.environ.get("DOMAIN_URL", "https://file-xor-web-3m61.onrender.com")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    MAX_FILE_SIZE = int(os.environ.get("MAX_FILE_SIZE", "2048"))  # in MB
    GEN_SECRET_KEY_LENGTH = int(os.environ.get("GEN_SECRET_KEY_LENGTH", "8"))
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "1"))  # in MB
    BIND_ADDRESS = os.environ.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(os.environ.get("PORT", "8000"))

    @classmethod
    def get_domain_url(cls) -> str:
        """Return configured DOMAIN_URL or fallback to runtime HOST_URL.

        Ensures no trailing slash and has scheme via URL utils where used.
        """
        if cls.DOMAIN_URL and str(cls.DOMAIN_URL).strip():
            return cls.DOMAIN_URL.strip()
        # Fallback from runtime.py if available
        host = load_host_url()
        return host or ""

class BotInfoConfig:
    # Bot related configurations    
    BOT_NAME = os.environ.get("BOT_NAME", "FILE XOR")
    BOT_LOGO = os.environ.get("BOT_LOGO", "https://files.catbox.moe/8cl88o.jpg")
    OWNER_ID = int(os.environ.get("OWNER_ID", "6146726705"))
    SUDO = list(map(int, os.environ.get("SUDO", "0").split(',')))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://frendz:243601@f2l.qwtj78t.mongodb.net/?appName=f2l")
    MODE = os.environ.get("MODE", "private").lower() 
    LANG = os.environ.get("LANG", "en")  # Default language code


LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'serverlogging.log',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
