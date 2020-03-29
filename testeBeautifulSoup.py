import requests

from bs4 import BeautifulSoup

urlGoogle = "https://www.google.com/search?q=16186544702"
resposta = requests.get(urlGoogle)
#print(resposta)
soup = BeautifulSoup(resposta.text, "html.parser")
#print(soup)
resultadoPesquisas = soup.find_all('div', class_ = "kCrYT")
#print(resultadoPesquisas)
#aqui ele verifica os resultados da pesquisa e se estiver tudo certo, salva no bd
for r in resultadoPesquisas:
	#print(r)
	try:
		link = r.find('a', href = True)['href'].strip("/url?q=")
		link = link.split("&")[0]
		titulo = r.find('div', class_ = "vvjwJb").get_text()
		
		if link != '' and titulo !='': 
			print(link)
			print(titulo)
	# se não salvar tenta o próximo
	except:
		continue