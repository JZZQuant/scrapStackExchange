from bs4 import BeautifulSoup
from urllib.request import urlopen


i=6000
f = open(r'C:\Users\Raghava\Desktop\Dump\DataAnalysis\DataDump\SourceForgeProjectList - Copy (7).txt','w')
while True :
    url = "http://sourceforge.net/directory/?page=" + i.__str__()
    pagecontent = urlopen(url)
    soup = BeautifulSoup(pagecontent)
    for link in soup.find_all('a'):
        projectpath = link.get('href')
        if projectpath.find('/?source=directory') > 0 :
            projectname = projectpath.split('/')[2] 
            f.write(projectname+'\n')        
    i = i+1 
    if i > 6999 :
        break 
f.close()  

