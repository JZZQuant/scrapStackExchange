from bs4 import BeautifulSoup 
import urllib2 


k=urllib2.urlopen("http://sourceforge.net/directory/language%3Aproglang_labview/?q=labview&page=3")
l = k.read()

soup = BeautifulSoup(l)
i = 0
for link in soup.find_all('a'):
	m= link.get('href')
	if m.find('/?source=directory') > 0 :
		print m
		i = i +1
print i
