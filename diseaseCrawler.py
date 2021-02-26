import requests
from bs4 import BeautifulSoup

from model import Disease, DBSession

pre = {'User-agent': 'Mozilla/5.0'}


def insertDisease(url):
    res = requests.get(url, headers=pre)
    rep = res.text
    try:
        soup = BeautifulSoup(rep, "html.parser")
        describe = soup.find('div', class_="message-boxs")
        data = soup.find_all('div', class_="list-label clear")
        disease = Disease(
            describe=str(describe.text.lstrip().rstrip()),
            standerName="无此属性",
            englishName="无此属性",
            diseaseCode="无此属性",
            aliasName="无此属性",
            shortName="无此属性",
            type="无此属性",
        )
        for i in data:
            name = i.find('span')
            value = i.find('div', class_="list-text").find('span').text
            if name.text == "【标准名称】：" and value != "":
                disease.standerName = value
                continue
            if name.text == "【英文名称】：" and value != "":
                disease.englishName = value
                continue
            if name.text == "【分类】：" and value != "":
                disease.type = value
                continue
            if name.text == "【别名】：" and value != "":
                disease.aliasName = value
                continue
            if name.text == "【疾病代码】：" and value != "":
                disease.diseaseCode = value
                continue
            if name.text == "【缩写名】：" and value != "":
                disease.shortName = value
                continue
        session = DBSession()
        session.add(disease)
        session.commit()
        session.close()
    except:
        print("获取失败")


def diseaseSpider(index):
    count = 0
    preUrl = "http://lczl.med.wanfangdata.com.cn/Resource/RightPart?dbtype=Disease&categoryId="
    requestUrl = preUrl + str(index)
    res = requests.get(requestUrl, headers=pre)
    rep = res.text
    try:
        soup = BeautifulSoup(rep, "html.parser")
        data = soup.find_all('a')
        preLink = "http://lczl.med.wanfangdata.com.cn"
        for i in data:
            link = preLink + str(i["href"])
            # 获取疾病的相关信息
            insertDisease(link)
            count = count + 1
    except:

        print("获取失败")
    return count


def runDiseaseSpider(index):
    count = 0
    for i in range(2, index):
        temp = diseaseSpider(i)
        count += temp
        print("疾病-" + str(i) + ": " + str(temp))
    print("共计导入：" + str(count))


if __name__ == '__main__':
    diseaseSpider(2)
