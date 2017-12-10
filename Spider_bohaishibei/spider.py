from bs4 import BeautifulSoup
import requests
import re

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def data_out(data):
    fo = open("./data.txt", "a+")

    fo.write("\n".join(data))

    fo.close()

def spider_src_page(page):
    req = requests.get(page)

    html_doc=str(req.content,'utf-8')
        # 在urlopen()添加context参数，请求将忽略网站的证书认证
        #html = BeautifulSoup(req.text)

    src = BeautifulSoup(html_doc, "lxml").select('body > section > div > div > article > p')

    data = []
    for s in src:
        if re.search("(?:支付宝)|(博海拾贝)|(未经允许)", s.get_text()):
            break

        ans = re.sub("(【\d+】)","",s.get_text())

        if s.get_text():
            data.append(ans)

        if s.find("img"):
            #print(s.img['src'])
            data.append("![]("+s.img['src']+")")
    data_out(data)

def spider_home_page(num):
    for i in range(num):
        req = requests.get("https://bohaishibei.com/post/category/main/"+"page/"+str(i)+"/")
        html_doc=str(req.content,'utf-8')
        src = BeautifulSoup(html_doc, "lxml").select("header > h2 > a")
        for link in src:
            #print(link.text)
            if re.search("(博海拾贝)", link.text):
                #print(link['href'])
                spider_src_page(link['href'])


if __name__ == "__main__":
    num = int(input("How many pages do you want to watch:"))
    spider_home_page(num)
    #print(data)
