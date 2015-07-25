from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.google.com/search?num=100&q=labview"
url2 = "https://www.codeplex.com/site/search?query=&sortBy=PublishedDate&page=0&size=100"
i=0
pagecontent = urlopen(url2)
soup = BeautifulSoup(pagecontent)
for link in soup.findAll('div'):
    projectpath = link.get('id')
    if projectpath == "search_directory_row":
        i=i+1
        print(i)
        try:
            print(link.find("p").contents)
            print(link.find('h3').find('a').contents)
            print(link.find('h3').find('a').get('href'))
        except :
            print('hello') 