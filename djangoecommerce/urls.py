from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.views.static import serve as serve_static
from django.contrib.auth.views import login, logout

from core import views
#from catalog import views as views_catalog

urlpatterns = [
    url(r'^$', views.index, name='index'), #dentro de views vai chamar a instancia index
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')), #as urls que começarem com produtos/ serão buscadas em catalog.urls
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^admin/', admin.site.urls),
]
