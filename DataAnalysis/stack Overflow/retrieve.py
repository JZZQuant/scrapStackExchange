from bs4 import BeautifulSoup
from urllib.request import build_opener


language = "labview"
pagestart = 1
pageend = 5
outputfile = r'c:\users\inmalikm\desktop\\' + language + ".txt"

url = "http://stackoverflow.com/questions/tagged/labview?pagesize=50&page="
file = open(outputfile, 'w+')
for i in range(pagestart,pageend):
    temp = url+str(i)
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Try/'+str(i)+".0")]
    response = opener.open(temp)
    soup = BeautifulSoup(response)
    for content in soup.findAll("div", attrs = {"class": "question-summary"}) :
            votes = content.find('span',attrs={"class":"vote-count-post "}).getText()
            answers = content.find('div',attrs={"class":"vote"}).find_next_sibling('div').getText()
            views = content.find('div',attrs={"class":"views"}).get('title')
            posttime = content.find('span',attrs={"class":"relativetime"}).get('title')
            file.write("votes: " + votes + " answers: " + answers + " views: "+ views+ " posttime: "+ posttime +"\n");
    print(i)       
file.close()
