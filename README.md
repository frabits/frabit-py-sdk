[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Build](https://github.com/frabits/frabit-py-sdk/actions/workflows/main.yml/badge.svg) 
![License: MIT](https://img.shields.io/github/license/frabits/frabit-py-sdk)
[![PyPI](https://img.shields.io/pypi/v/frabit)](https://pypi.org/project/frabit/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/frabit)](https://pypi.org/project/frabit)  

# frabit-py-sdk
Frabit official python sdk

## Supported Python Versions
This SDK supports the following Python implementations:

Python 3.6
Python 3.7
Python 3.8
Python 3.9
Python 3.10

# Installation

Install from source code
```bash
git clone https://github.com/frabits/frabit-py-sdk.git 
cd frabit-py-sdk && python setup.py install
```
Install from PyPi
```bash
pip install frabit
```

# Examples

```python
import os
from frabit import Client

base_url = os.environ.get('FRABIT_BASE_URL') or "api.frabit.tech"
token = os.environ.get('FRABIT_TOKEN') or  ""
client = Client(base_url,token)
client.database.get()
```