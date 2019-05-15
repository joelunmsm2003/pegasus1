#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests

import json

n=0


url = ['https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/surco','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/san-isidro','https://www.photokinesiologas.com/kinesiologas/surquillo','https://www.photokinesiologas.com/kinesiologas/lince','https://www.photokinesiologas.com/kinesiologas/san-juan-de-miraflores','https://www.photokinesiologas.com/kinesiologas/cerca_-12.1061142,-77.0307285,3',u'https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/18-21-años','https://photokinesiologas.com/kinesiologas/lima-metropolitana/san-martin-de-porres','https://photokinesiologas.com/kinesiologas/lima-metropolitana/venezolanas','https://photokinesiologas.com/kinesiologas/lima-metropolitana/','https://photokinesiologas.com/kinesiologas/','https://photokinesiologas.com/']


for u in url:


	try:

		r  = requests.get(u)

		data = r.text

		soup = BeautifulSoup(data)

	except:

		data = ''

		soup = BeautifulSoup(data)


	for link in soup.find_all('a', class_='link_anuncio'):

		print link.get('href')

		try:

			url = 'https://photokinesiologas.com'+link.get('href')

			x = requests.get(url)

			datax = x.text

			soupx = BeautifulSoup(datax)

		

			_telefono=[]

			for wsp in soupx.find_all('span', class_='boton_telefono whatsapp'):

				try:

					telefono =  wsp.get('data-telefono')

					_telefono.append(telefono)

				except:

					pass


			total_cont_anuncio =[]

			for anuncio in soupx.find("div", {"id": "anuncio_texto"}):

				try:

					cont_anuncio =  anuncio.get_text()

					total_cont_anuncio.append(cont_anuncio)

				except:

					pass


			imagenes = []

			for sobremi in soupx.find("div", {"class": "contenedor"}):

				try:

					imagen= sobremi.get('src')

					imagenes.append(imagen)

				except:

					pass

			listdetalle=[]

			for detalle in soupx.find_all("a", {"class": "anuncio_categoria categoria_sel_off"}):

				try:

					detalle= detalle.get_text()

					listdetalle.append(detalle)

				except:

					pass




			for phone in soupx.find("td", {"class": "boton_texto"}):

				try:

					fono = phone

				except:

					pass

			contenido = json.dumps({'wsp':_telefono,'anuncio':total_cont_anuncio,'imagenes':imagenes,'detalle':listdetalle,'fono':fono})

			#print contenido


			print '----------------------'

			try:

				dat= requests.get('http://mylookxpressapp.com:2000/verificatelefono/'+str(telefono))

				print dat.text

				if dat.text!='"no"':

					print 'Entre..... =)'

					cc = requests.post('http://mylookxpressapp.com:2000/photoguardaurlphoto', data = {'url':url,'contenido':contenido})

			except:

				print 'Hay un error =('

		except:

			pass


			

