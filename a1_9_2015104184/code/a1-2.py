from bs4 import BeautifulSoup
import urllib.request as req

url = "http://info.finance.naver.com/marketindex/"

html = req.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

usd = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print('USD: ', usd.text, 'WON')
