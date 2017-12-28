from bs4 import BeautifulSoup
import requests
import json
import pprint

def test():
    data = []

    # with open('cookie.json','w') as f:
    #     json.dump(cookie,f)

    with open('cookie.json','r') as f:
        cookie = json.load(f)
    #pprint.pprint(cookie)

    req = requests.get("http://jwxt.bupt.edu.cn/xtcxAction.do?totalrows=186&page=1&pageSize=186",cookies=cookie)

    f = open("./index.html","a+")
    f.write(req.text)
    f.close()

    # html = BeautifulSoup(str(req.content,"GBK"), "lxml")
    # #print(html.prettify())
    # doc = html.select("html body form#search table.titleTop2 tbody tr td.pageAlign table#user.displayTag tbody tr.odd")
    # print(doc)
    # for i in html.select("table.titleTop2:nth-child(12) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(2)"):
    #     print(i)

if __name__ == "__main__":
    test()
