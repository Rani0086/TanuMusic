#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/TanuMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/TanuMusic/blob/master/LICENSE >
#
# All rights reserved.
from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("✦ Connecting to your Mongo Database...💛")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("✦ Connected to your Mongo Database...❤️")
except:
    LOGGER(__name__).error("✦ Failed to connect to your Mongo Database...💚")
    exit()
