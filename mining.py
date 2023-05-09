from newspaper import Article
import requests
from bs4 import BeautifulSoup
import nltk
# import pydoop.hdfs as hdfs
import subprocess

nltk.download('punkt')
#A new article from TOI
URL="https://timesofindia.indiatimes.com/"
r=requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup)
mydivs = soup.find_all("a",class_="Hn2z7 undefined")
urls=[i['href'] for i in mydivs]
# urls=[
# # "https://timesofindia.indiatimes.com/india/rahul-gandhis-plea-against-conviction-in-defamation-case-gujarat-hc-to-resume-hearing-on-may-2/articleshow/99866262.cms",
# # "https://timesofindia.indiatimes.com/city/delhi/peacock-feathers-inspire-hues-of-rapidx-stations/articleshow/99858147.cms",
# # "https://timesofindia.indiatimes.com/city/raipur/explosive-planted-in-dantewada-2-months-before-blast-say-police/articleshow/99856741.cms"

# ]
# url = "https://timesofindia.indiatimes.com/india/rahul-gandhis-plea-against-conviction-in-defamation-case-gujarat-hc-to-resume-hearing-on-may-2/articleshow/99866262.cms"
for url in urls[:3]:
    #For different language newspaper refer above table
    toi_article = Article(url, language="en") # en for English

    #To download the article
    toi_article.download()

    #To parse the article
    toi_article.parse()

    #To perform natural language processing ie..nlp
    toi_article.nlp()

    #To extract title
    print("Article's Title:")
    print(toi_article.title)
    print("n")
    with open("/home/neetigya/DSLab/news.txt","+a") as f:
        f.write(toi_article.text)
        f.write("\n")
    #To extract text
    print("Article's Text:")
    print(toi_article.text)
    print("n")

    #To extract summary
    print("Article's Summary:")
    print(toi_article.summary)
    print("n")

    #To extract keywords
    print("Article's Keywords:")
    print(toi_article.keywords)

output = subprocess.Popen(["hdfs","dfs", "-mkdir", "/user"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output = subprocess.Popen(["hdfs","dfs", "-mkdir", "/user/input"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


output = subprocess.Popen(["hdfs","dfs", "-put", "/home/neetigya/DSLab/news.txt","/user/input"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


