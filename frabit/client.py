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


class Client:
    """Communicate with frabit via RestAPI"""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

        self._database = None
        self._backup = None

    @property
    def database(self):
        """
        Access the hedera_mirror_sdk Account API
        """
        if self._database is None:
            from frabit.database import Database
            self._database = Database(self, self.base_url, 'database', self.hedera_mirror_sdk_version)
        return self._database
