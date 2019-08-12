import requests 

res = requests.get("https://fb.com/emmawatson")
try :
    res.raise_for_status
except Exception as ex :
    print("%s"%(ex))

soemthing = open("REmo.txt",'wb')
for chunk in res.iter_content(10000):
    soemthing.write(chunk)

soemthing.close()