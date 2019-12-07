from bs4 import BeautifulSoup

import requests

n=0
for n in range(0,100):

	print 'NNNNNN:',n


	if n==0:

		r  = requests.get("https://www.locanto.com.pe/Chica-busca-chico/202/")

	else:

		r  = requests.get("https://www.locanto.com.pe/Chica-busca-chico/202/"+str(n))

	data = r.text

	soup = BeautifulSoup(data)

	



	for link in soup.find_all('a', class_='bp_ad__link'):
	    
		url = link.get('href')

		x = requests.get(url)

		datax = x.text

		soupx = BeautifulSoup(datax)

		

		for d in soupx.find_all('div', class_='breadcrumb_item'):



			distrito =len(str(d).split('Lima'))

		print 'entre'

		for linkx in soupx.find_all('div', class_='user_content'):

			contenido = str(linkx)

			contenido = contenido.replace('<div class="user_content" id="js-user_content" itemprop="description">','').replace('<br>','').replace('<br/>','').replace('  ','').replace('<div>','').replace('</div>','')


		
		cc = requests.post('http://mylookxpressapp.com:2000/guardaurl', data = {'url':url,'contenido':contenido})



