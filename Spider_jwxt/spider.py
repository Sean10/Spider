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

    f = open("./1.html","w")
    f.write(req.text)
    f.close()

if __name__ == "__main__":
    test()
