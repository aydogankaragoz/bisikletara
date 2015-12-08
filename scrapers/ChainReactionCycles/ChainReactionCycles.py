from bs4 import BeautifulSoup
import requests
import urllib2
import pickle

base_url = 'http://www.chainreactioncycles.com/tr/en/'
number_of_products = 0
big_list = []
for row in open('ChainReactionCycles.txt'):
#for row in ['http://www.chainreactioncycles.com/tr/en/road-bikes']:
    category = row.strip()
    category = category.lower()
    category = category.replace(' & ', ' ').replace(' - ', ' ').replace(' ', '-').replace('_', '-')
    print category
    url = base_url + category
    page_url = url
    page_number = 1
    while True:
        req = urllib2.urlopen(page_url)
        html = req.read()
        soup = BeautifulSoup(html)

        product_divs = soup.find_all('div', {"class": "products_details product_details_plp"})

        for product_div in product_divs:
            description = product_div.find('li', {'class': 'description'})

            link = description.find('a')
            fulllink = link.get('href')

            price = product_div.find('li', {'class': 'fromamt'})

            img = product_div.find('img').get('src')

            try:
                a_dict = {}
                #print str(number_of_products+1)
                a_dict['name'] = description.text.strip().replace('\n', ' ')
                a_dict['price'] = price.text.strip()
                a_dict['link'] = 'http://www.chainreactioncycles.com' + str(fulllink)
                a_dict['img'] = img
                number_of_products += 1
                big_list.append(a_dict)
                #print a_dict
            except:
                print description
                continue
        print str(len(product_divs)) + '\t' + str(page_url)
        if len(product_divs) < 48:
            break
        else:
            page_number += 1
            page_url = url + '?page=' + str(page_number)
pickle.dump(big_list, open("ChainReactionCycles.p", "wb"))
