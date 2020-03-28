from background_task import background

import logging
logger = logging.getLogger(__name__)

@background(schedule=10)
def realiza_crawler_google(nomeCliente, cpfCliente):
	if(cpfCliente ==''):
		user = User.objects.get(nome=nomeCliente)
	else:
		user = User.objects.get(cpf=cpfCliente)
	
	#aqui realiza a pesquisa no google
	
	#aqui salva as informações no bd
	