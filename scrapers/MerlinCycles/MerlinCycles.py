from bs4 import BeautifulSoup
import requests
import urllib2
import pickle

number_of_products = 0
big_list = []
for row in open('MerlinCycles.txt'):
#for row in ['https://www.merlincycles.com/factory-road-wheels-75320/']:
    url = row.strip()
    req = urllib2.urlopen(url)
    html = req.read()
    soup = BeautifulSoup(html)
    
    try:
        product_div = soup.find_all('ul', {"class": "products"})
        products = product_div[-1].find_all('li')

        for product in products:
            try: 
                a_dict = {}
                print str(number_of_products+1)
             
                full_link = product.find("h2").a.get('href')
                title = product.find("h2").a.get('title')
          
                img_link = product.find_all('img')[-1].get('src')
          
                price = product.find('span', {'class': 'merlin-price'}).text
                a_dict['name'] = title
                a_dict['price'] = price
                a_dict['link'] = full_link
                a_dict['img'] = img_link
                big_list.append(a_dict)
                number_of_products += 1
            except:
                print 'ic hata'
    except:
        print 'hata'
pickle.dump(big_list, open("MerlinCycles.p", "wb"))
