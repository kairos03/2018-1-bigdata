from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
data = req.urlopen(url)

soup = BeautifulSoup(data, 'html.parser')

title = soup.find('title').text
wf = soup.find('wf').text

print(title)
print(wf)