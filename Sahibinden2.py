import re
from bs4 import BeautifulSoup as bs
import urllib.request

# -*- coding: cp1254 -*-
#conn= pymysql.connect(host='localhost',user='burhan',password='a123456',db='bitirme',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)


sonuc=open('sonuc2.csv','w')
sonuc.write('marka,model,yıl,kilometre,renk,fiyat,il,yakit,vites')
sonuc.write('\n')
yakitx=''
vitesx=''
#Getting full page to scrape
def getSoup(url):
    req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    )
    resp = urllib.request.urlopen(req)
    soup = bs(resp,'lxml')
    return soup




#Getting spesific informations from soup
def getBrands(url):
    soup = getSoup(url+'/'+yakit+'/'+vites)
    brands = soup.find_all('li', class_='cl2')
    brandLinks=[]
    for b in brands:
        brandLinks.append('https://www.sahibinden.com'+b.find('a').get('href'))
    return brandLinks

def getModels(url):
    soup = getSoup(url)
    models = soup.find_all('li', class_='cl3')
    modelLinks=[]
    x=(len(models)/2)
    for m in models[int(x):]:
        modelLinks.append('https://www.sahibinden.com'+m.find('a').get('href')+'?pagingOffset=0')
    return modelLinks

def getCars(url):
    offSet=0
    urlx=url
    while(True):
        #print(urlx)
        urlx=urlx[:urlx.index('=')+1]+str(offSet)
        soup = getSoup(urlx)
        n=re.findall('\d+', soup.find('div',class_='result-text').text.replace('.',''))
        #print(soup.find('div',class_='result-text').text.replace('.',''))
        a=int(n.pop())
        print(offSet)
        print(urlx)
        #print(url+'ilan adedi:'+str(a))
    #cars = soup.find_all('tr', class_='searchResultsItem     ')
    #carsBold = soup.find_all('tr', class_='searchResultsItem searchResultsPromoHighlight searchResultsPromoBold   ')
        b=soup.find_all('li', class_='cl2')
        m=soup.find_all('li', class_='cl3')
        brand= b[1]

        model = m[1]
        brand=brand.text.strip()
        model=model.text.strip()
        dt=[]
    #for c in cars:
    #    details.append(c.find_all('td', class_='searchResultsAttributeValue'))
        cars = soup.find_all('td', class_='searchResultsAttributeValue')
        prices = soup.find_all('td', class_='searchResultsPriceValue')
        locations = soup.find_all('td', class_='searchResultsLocationValue')
        i=0
        details = brand+','+model
        det=''
        for c in cars:

            car=c.text
            det=det+car.replace('                    ',',').strip()
            i=i+1
            if i is 3:
                details=details+det
                details=details+','+prices.pop(0).text.strip()
                details=details+','+locations.pop(0).text.strip()
                details=details+','+yakit+','+vites
                i=0
                det=''
                #dt.append(details)
                try:
                    sonuc.write(details)
                    sonuc.write('\n')
                except UnicodeEncodeError:
                    pass                
                details = brand+','+model
        offSet=offSet+20

        if offSet >= a:
            break

yakit='benzin'
vites='manuel'
for model in getBrands('https://www.sahibinden.com/otomobil/benzin/manuel'):
    for d in getModels(model):
        getCars(d)
yakit='benzin-lpg'
vites='manuel'
for model in getBrands('https://www.sahibinden.com/otomobil/benzin-lpg/manuel'):
    for d in getModels(model):
        getCars(d)
yakit='dizel'
vites='manuel'
for model in getBrands('https://www.sahibinden.com/otomobil/dizel/manuel'):
    for d in getModels(model):
        getCars(d)
yakit='hybrid'
vites='manuel'
for model in getBrands('https://www.sahibinden.com/otomobil/hybrid/manuel'):
    for d in getModels(model):
        getCars(d)
yakit='benzin'
vites='yari-otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/benzin/yari-otomatik'):
    for d in getModels(model):
        getCars(d)
yakit='benzin-lpg'
vites='yari-otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/benzin-lpg/yari-otomatik'):
    for d in getModels(model):
        getCars(d)
yakit='dizel'
vites='yari-otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/dizel/yari-otomatik'):
    for d in getModels(model):
        getCars(d)
yakit='hybrid'
vites='yari-otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/hybrid/yari-otomatik'):
    for d in getModels(model):
        getCars(d)
yakit='benzin'
vites='otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/benzin/otomatik'):
    for d in getModels(model):
        getCars(d)
yakit='benzin-lpg'
vites='otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/benzin-lpg/otomatik'):
    for d in getModels(model):
        getCars(d)
yakit='dizel'
vites='otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/dizel/otomatik'):
    for d in getModels(model):
        getCars(d)
yakit='hybrid'
vites='otomatik'
for model in getBrands('https://www.sahibinden.com/otomobil/hybrid/otomatik'):
    for d in getModels(model):
        getCars(d)



sonuc.close()
print('tamamlandı')
