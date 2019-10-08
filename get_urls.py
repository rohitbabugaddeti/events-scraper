import requests
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

def is_url_ok(url):
    try:
        return 200 == requests.head(url).status_code
    except Exception:
        return False

def get(url):
    if (is_url_ok(url)):
        res=Request(url=url,headers=headers)
        print("making request..")
        content=urlopen(res)
        parsable=BeautifulSoup(content,'html.parser')
        print("parsing content...")
        a=parsable.find_all('a')
        print("building urls...")
        urls=[each.get('href') for each in a if '/event/' in each.get('href')]
        urls=[url if "https" in url else url.replace('http','https') for url in urls]
        # print(urls)
        # print(len(urls))
        print("building urls done.")
        return urls
    else:
        print("URL may be dead/not working")

def get_in(url):
    if (is_url_ok(url)):
        res=Request(url=url,headers=headers)
        print("making request..")
        content=urlopen(res)
        parsable=BeautifulSoup(content,'html.parser')
        print("parsing content..")
        a=parsable.find_all('a',attrs={'class':""})
        print("building urls...")
        urls=["https://insider.in"+each.get('href') for each in a if '/event' in each.get('href')]
        print("building urls done.")
        return urls
    else:
        print("URL may be dead/not working")