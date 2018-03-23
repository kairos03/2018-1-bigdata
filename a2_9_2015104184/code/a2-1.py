from urllib.parse import *
base = "http://example.com/html/a.html"

print(urljoin(base, "../index.html"))
print(urljoin(base, "../css/hoge.css"))