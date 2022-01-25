#!/usr/bin/python3

import requests as req
import urllib
from urllib.parse import quote
import sys
import warnings
warnings.filterwarnings("ignore")

if len(sys.argv) <= 1:
    print(f'USAGE: python3 {sys.argv[0]} <url>')
    exit(1)

payload = f'xxx'
payload = urllib.parse.quote(payload)

url = f'{sys.argv[1]}/xxx{payload}'
resp = req.get(url, verify=False)

print(resp.elapsed)
