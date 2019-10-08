from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
def get(url):
    session=HTMLSession()
    resp=session.get(url)
    resp.html.render()
    return resp.html.html