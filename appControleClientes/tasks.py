from background_task import background
from .models import RegistroGoogleCliente,Cliente
import requests

from bs4 import BeautifulSoup

import logging
logger = logging.getLogger(__name__)

@background(schedule=10)
def realiza_crawler_google(nomeCliente, cpfCliente):
	try:
		if(cpfCliente ==''):
			userT = Cliente.objects.get(nome=nomeCliente)
			pesquisa = nomeCliente
		else:
			userT = Cliente.objects.get(cpf=cpfCliente)
			pesquisa = cpfCliente
	except:
		#da erro se não encontrar cliente, então só não executa
		return
		
	#realiza a pesquisa
	urlGoogle = "https://www.google.com/search?q=" + pesquisa
	resposta = requests.get(urlGoogle)
	soup = BeautifulSoup(resposta.text, "html.parser")

	resultadoPesquisas = soup.find_all('div', class_ = "kCrYT")
	#aqui ele verifica os resultados da pesquisa e se estiver tudo certo, salva no bd
	for r in resultadoPesquisas:
		try:
			link = r.find('a', href = True)['href'].strip("/url?q=")
			link = link.split("&")[0]
			titulo = r.find('div', class_ = "vvjwJb").get_text()
			if link != '' and titulo !='': 
				print(link)
				print(titulo)
				registroGoogle = RegistroGoogleCliente(user=userT,url=link,nomeLink=titulo)
				registroGoogle.save()
		# se não salvar tenta o próximo
		except:
			continue
	