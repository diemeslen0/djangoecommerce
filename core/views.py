#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import ContactForm

User = get_user_model()

class IndexView(TemplateView):

    template_name = 'index.html' #renderiza um template (por causa da TemplateView)

#essa variável index está sendo chamada em urls.py como views.index
index = IndexView.as_view() 

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
        form = ContactForm()#limpa o formulário depois de submetido
        messages.success(request, 'Enviado com sucesso!')
    elif request.method == request.POST:
        messages.error(request, 'Formulário inválido')
    context = {
		'form': form,
		'success': success
	}
    return render(request, 'contact.html', context)