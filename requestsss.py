#! python3.7

import requests

res = requests.get("https://www.facebook.com/emma watson")
print(res.status_code)
try :
    res.raise_for_status()
except Exception as exc:
    print("%s "%(exc)) 
