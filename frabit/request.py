# Frabit - The next-generation database automatic operation platform
# Copyright © 2022-2024 Frabit Team
#
# Licensed under the GNU General Public License, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	https://www.gnu.org/licenses/gpl-3.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

import frabit
from typing import Dict

from frabit.version import get_version


class Request:
    """request wrapper """
    def __init__(self, path: str, params: Dict, verb: str):
        self.path = path
        self.params = params
        self.verb = verb

    def make_request(self, url: str):
        headers = self.__get_headers()
        params = self.params
        verb = self.verb

        try:
            return requests.request(verb, url, json=params, headers=headers)
        except requests.HTTPError as e:
            raise e

    def do(self):
        resp = self.make_request(url=f"{frabit.api_url}{self.path}")

        # delete calls do not return a body
        if resp.text == "" and resp.status_code == 200:
            return None

        # handle error in case there is a statusCode attr present
        # and status != 200
        if resp.status_code != 200 and resp.json().get("statusCode"):
            error = resp.json()
        return resp.json()

    @staticmethod
    def __get_headers(self) -> Dict:
        """get_headers returns the HTTP headers that will be
        used for every req.

        Returns:
            Dict: configured HTTP Headers
        """
        return {
            "Accept": "application/json",
            "Authorization": f"Bearer ",
            "User-Agent": f"frabit-py:{get_version()}",
        }

