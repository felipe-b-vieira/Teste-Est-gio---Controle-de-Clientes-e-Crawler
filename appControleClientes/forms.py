from django import forms


class CrawlerForm(forms.Form):
	nome = forms.CharField(label='Nome', max_length=100)
	cpf = forms.CharField(label='CPF', max_length=100)