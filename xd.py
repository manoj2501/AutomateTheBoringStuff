#! python3

# download python 

import requests,os,bs4
url = 'https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#') :
    # download the page internally not int 
    print("Downloading page %s"%url) 
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # find and download the image
    comicElem = soup.select('#comic img')
    if comicElem == [] :
        print("Coludn't find the image ")
    else :
        comicUrl = 'http:'+ comicElem[0].get('src')
        # Downlad the image 
        print('Dwomnloading the image %s'%comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()


        # save the iamge to the xkcd 
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000) :
            imageFile.write(chunk)
        imageFile.close()
    prevlink =soup.select('a[rel="prev"]')[0]
    url ='http://xkcd.com'+prevlink.get('href')

print('Done.')
