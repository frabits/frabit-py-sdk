# (c) 2020 frabit-server Project maintained and limited by FrabiTech < blylei.info@gmail.com >
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This file is part of frabit-server
#
import os

from version import get_version
from client import Client


api_key = os.environ.get("FRABIT_API_KEY")
api_url = os.environ.get("FRABIT_API_URL", "https://api.frabit.tech")

__all__ = [
    "get_version",
    "Client",
]
