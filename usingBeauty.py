import requests,bs4

res = requests.get("https://www.facebook.com/pg/emmawatson/photos/?ref=page_internal")
res.raise_for_status()
emmaSoup = bs4.BeautifulSoup(res.text)
emmaSoup.select('img')