#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/TanuMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/TanuMusic/blob/master/LICENSE >
#
# All rights reserved.
import os

from ..logging import LOGGER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("❖ Directories Updated...🧡")
