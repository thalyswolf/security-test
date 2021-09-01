from bs4 import BeautifulSoup
import requests
import sys

html_request = requests.get(sys.argv[1])
obj_soup = BeautifulSoup(html_request.content)

links = []

for link in obj_soup.findAll("a"):
    print link
    if 'href' in link.attrs and link.attrs['href'] is not None:
        if link.attrs['href'] not in links:
            links.append(link.attrs['href'])

print(links)