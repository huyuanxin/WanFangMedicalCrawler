from drugCrawler import runDrugSpider
from examinationCrawler import runExaminationSpider
from diseaseCrawler import runDiseaseSpider

if __name__ == '__main__':
    runDiseaseSpider(500)
    runExaminationSpider(500)
    runDrugSpider(500)
