# A text file from a URL can be accessed using urllib.

# Make sure both the packages are installed
import urllib3
from bs4 import BeautifulSoup
pool_object = urllib3.PoolManager()
target_url = 'http://httpbin.org/robots.txt'
response_ = pool_object.request('GET', target_url)
print("Status: ", response_.status)
final_html_txt = BeautifulSoup(response_.data)
print("ḦTML: ", final_html_txt)
raw_data = response_.data
print("Raw Text: ", raw_data)