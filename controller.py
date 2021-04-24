import urllib.request
from bs4 import BeautifulSoup

def get_data(x):
    try:
        response =  urllib.request.urlopen(x)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        # print(soup)
        title = soup.find("title").text
        url = soup.find("meta",  property="og:url")
        thumbnail=soup.find("meta",property='og:image')
        des=soup.find('meta',attrs={'name':'description'})
        try:
            res=urllib.request.urlopen(thumbnail['content'])
            thumbnail=thumbnail['content']
        except Exception as e:
            print(e)
            thumbnail=str(url['content'])+str(thumbnail['content'])
        return ({
            'done':True,
            "title": title,
            "url":url and url['content'],
            "thumbnail":thumbnail,
            "descrp": des and des['content']
        })
    except Exception as e:
        print(e)
        return {
            'done':False,
            "message":"Preview not available!"
        }
