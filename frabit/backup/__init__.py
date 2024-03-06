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

from frabit.request import Request


class Backup:
    """Access Backup asset via this endpoint"""
    def __init__(self):
        pass

    def get_backup(self):
        """list a backup set """
        Request.do()

    def get_backups(self):
        pass

    def get_backup_by_id(self):
        pass

    def get_backup_name(self):
        pass

    def make_backup(self):
        pass

    def delete_backup(self):
        pass

    def cancel_backup(self):
        pass
