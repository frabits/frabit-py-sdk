#!/usr/bin/env python
# Frabit - The next-generation database automatic operation platform
# Copyright © 2022-2024 Frabit Team
#
# Licensed under the GNU General Public License, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.gnu.org/licenses/gpl-3.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

from frabit.version import get_version

install_requires = "requests==2.27.1"

setup(
    name="frabit",
    version=get_version(),
    description="Frabit Python SDK",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    author="frabit team",
    author_email="blylei.info@gmail.com",
    url="https://github.com/frabits/frabit-py-sdk",
    packages=["frabit"],
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    python_requires=">=3.7",
    keywords=["database", "automatic"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
