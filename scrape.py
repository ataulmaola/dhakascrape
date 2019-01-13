from bs4 import BeautifulSoup
import requests
import re
import csv

main="https://www.dhakatribune.com"


urls = ["https://www.dhakatribune.com/articles/opinion/op-ed/page/{}".format(i) for i in range(1, 282)]
headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})


with open('result.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['title','link','content','writer_l']) # write header once
    for url in urls:
    	response = requests.get(url, headers=headers)
    	soup = BeautifulSoup(response.text, "html.parser")
    	items = soup.find_all('div', 'top-news-cont list-para')
    	for item in items:
    		ur=item.find('a',href=True)
    		title=item.find('h4','news-title').text
    		link=main+ur.get('href')
    		resp = requests.get(link, headers=headers)
    		oup = BeautifulSoup(resp.text, "html.parser")
    		main_content=oup.find('div','report-content fr-view')
    		highlight=main_content.find('div','highlighted-content')
    		content=main_content.text
    		#entries = soup.find_all('div', class_='deleadres')
    		writer_l=oup.find('em').text
    		w.writerow([title,link,content,writer_l]) # write data rows for each entry
