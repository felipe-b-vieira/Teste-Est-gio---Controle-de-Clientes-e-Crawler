from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .tasks import realiza_crawler_google
from .forms import CrawlerForm

import logging
logger = logging.getLogger(__name__)


#formulario do crawler, ele vai ativar a background task do crawler com base nas informações do crawler
def ativa_crawler(request):
    if request.method == 'POST':
        form = CrawlerForm(request.POST)
        if form.is_valid():
            realiza_crawler_google(form.cleaned_data['nome'],form.cleaned_data['cpf'])
            return render(request, 'crawlerAtivado.html')
    else:
        form = CrawlerForm()

    return render(request, 'crawler.html', {'form': form})
	
