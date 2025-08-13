# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26176218")
API_HASH = os.environ.get("API_HASH", "4a50bc8acb0169930f5914eb88091736")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8271624089:AAHReeFOBWExbuPFVz7opSf52q6B8gHDcyQ")
FORCE_SUB = os.environ.get("FORCE_SUB", "fpflims")

DB_NAME = os.environ.get("DB_NAME", "kevyabdi20")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://kevyabdi20:<kevyabdi20>@kevyabdi.mymiztp.mongodb.net/?retryWrites=true&w=majority&appName=kevyabdi")

FLOOD = int(os.environ.get("FLOOD", "10"))
START_PIC = os.environ.get("START_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
PORT = os.environ.get("PORT", "8080")