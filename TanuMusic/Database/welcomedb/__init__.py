from async_pymongo import AsyncClient
from config import MONGO_DB_URI

DBNAME = "TANUMUSIC"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
