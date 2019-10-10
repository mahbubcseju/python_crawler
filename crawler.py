import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    print(WebUrl)
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        #print(s)
        all_ = s.findAll('div', {'class':'rnkRanking_top3box'}) + s.findAll('div', {'class':'rnkRanking_after4box'})
        for link in all_:
            #print(link)
            pri = link.findAll('div', {'class':'rnkRanking_price'})[0].text
            print(pri)
            pri = link.findAll('div', {'class':'rnkRanking_imageBox'})
            images = pri[0].findAll('img')
            print(images[0]["src"])
       


for j in range(1,13):
    web(1,"https://ranking.rakuten.co.jp/daily/100939/p="+str(j)+"/")

