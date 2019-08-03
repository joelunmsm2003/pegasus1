#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests

import json


url = 'https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/lince/mujer-muy-apasionada-esta-en-busqueda-de-una-buena-compa%C3%B1ia-para-hacer-cositas-ricas-id-hc5a9'

x = requests.get(url)

datax = x.text

soupx = BeautifulSoup(datax)




c=0

for m in soupx.find_all('meta'):

	c=c+1


	if c==9:

		coordenadas = m['content']
		print c,m["content"]


for f in soupx.find("div", {"class": "bloque_tarifas"}):

	print f.text

