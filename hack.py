import requests
import sys
res=requests.get("10.10.11.161/api")
print(res.text)
