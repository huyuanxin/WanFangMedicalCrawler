import requests
from bs4 import BeautifulSoup

from model import Drug, DBSession

pre = {'User-agent': 'Mozilla/5.0'}


def insertDrug(url):
    res = requests.get(url, headers=pre)
    rep = res.text
    try:
        soup = BeautifulSoup(rep, "html.parser")
        describe = soup.find('div', class_="message-boxs")
        data = soup.find_all('div', class_="list-label clear")
        drug = Drug(
            describe=str(describe.text.lstrip().rstrip().replace("<sub>", "").replace("</sub>", "")),
            standerName="无此属性",
            englishName="无此属性",
            type="无此属性",
            aliasName="无此属性",
        )
        for i in data:
            name = i.find('span')
            value = i.find('div', class_="list-text").find('span').text
            if name.text == "【标准名称】：" and value != "":
                drug.standerName = value
                continue
            if name.text == "【英文名称】：" and value != "":
                drug.englishName = value
                continue
            if name.text == "【分类】：" and value != "":
                drug.type = value
                continue
            if name.text == "【别名】：" and value != "":
                drug.aliasName = value
                continue
        session = DBSession()
        session.add(drug)
        session.commit()
        session.close()
    except:
        print(res.url)
        print("获取失败")


def drugSpider(index):
    count = 0
    preUrl = "http://lczl.med.wanfangdata.com.cn/Resource/RightPart?dbtype=Drug&categoryId="
    requestUrl = preUrl + str(index)
    res = requests.get(requestUrl, headers=pre)
    rep = res.text
    try:
        soup = BeautifulSoup(rep, "html.parser")
        data = soup.find_all('a')
        preLink = "http://lczl.med.wanfangdata.com.cn"
        for i in data:
            link = preLink + i["href"]
            insertDrug(link)
            count = count + 1
    except:
        print("获取失败")

    return count


def runDrugSpider(index):
    count = 0
    for i in range(1, index):
        temp = drugSpider(i)
        count += temp
        print("药品-" + str(i) + ": " + str(temp))
    print("共计导入：" + str(count))


if __name__ == '__main__':
    drugSpider(39)