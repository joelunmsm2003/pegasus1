#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests

import json

n=0


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



#url = ['https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/surco','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/san-isidro','https://www.photokinesiologas.com/kinesiologas/surquillo','https://www.photokinesiologas.com/kinesiologas/lince','https://www.photokinesiologas.com/kinesiologas/san-juan-de-miraflores','https://www.photokinesiologas.com/kinesiologas/cerca_-12.1061142,-77.0307285,3',u'https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/18-21-años','https://photokinesiologas.com/kinesiologas/lima-metropolitana/san-martin-de-porres','https://photokinesiologas.com/kinesiologas/lima-metropolitana/venezolanas','https://photokinesiologas.com/kinesiologas/lima-metropolitana/','https://photokinesiologas.com/kinesiologas/','https://photokinesiologas.com/']

url=['https://pe.skokka.com/kinesiologas/?p=1','https://pe.skokka.com/kinesiologas/?p=3','https://pe.skokka.com/kinesiologas/?p=4']

for x in range(100):

	u='https://pe.skokka.com/kinesiologas/lima-metropolitana/?p='+str(x+1)

	#print u


	try:

		r = requests.get(u, headers=headers)

		data = r.text

		#print 'jajaj',data

		soup = BeautifulSoup(data)

	except:

		data = ''

		soup = BeautifulSoup(data)



	for link in soup.find_all('div', class_='immagine'):

		soup =  BeautifulSoup(str(link))

		for a in soup.find_all('a'):

			url= a.get('href')


			try:

				x = requests.get(url, headers=headers)

				datax = x.text

				#print datax

				soupx = BeautifulSoup(datax)

				imagenes=[]
				
				for i in soupx.find_all('img', class_='lazy'):

					try:

					
						imagenes.append(i.get('src'))


					except:

						pass

				for h in soupx.find_all('a', class_='telefono'):

					try:

						#print 'QUeee.',h.get('href').split('tel')[1]
						fono = h.get('href').split('tel:')[1]

					except:

						pass

				detalle=[]

				for d in soupx.find_all('div',class_='descrizione'):

					try:

						zona = BeautifulSoup(str(d)).find_all('li')[1].text.split(':')[1]

						cont_anuncio = BeautifulSoup(str(d)).find_all('p')[0].text+' '+zona

						edad = BeautifulSoup(str(d)).find_all('li')[0].text.split(':')[1]

						detalle.append(zona)
						detalle.append(zona)
						detalle.append('')
						detalle.append('')
						
						detalle.append('')

					except:

						pass


				contenido = json.dumps({'wsp':fono,'anuncio':cont_anuncio,'imagenes':imagenes,'fono':fono,'detalle':detalle})
				
				try :

					dat= requests.get('http://mylookxpressapp.com:2000/verificatelefono/'+str(fono))


					if dat.text!='"no"':

						print 'Entre..... =)'

						cc = requests.post('http://mylookxpressapp.com:2000/guardaskoka', data = {'url':url,'contenido':contenido})

				except:

					print 'Hay un error =('

			except:

				pass


			

