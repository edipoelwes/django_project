#from django.contrib import admin
from django.urls import path, include
#from News.views import home, contato
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('novidades', views.Novidade_datalhes, name='novidades'),
    #path('admin/', admin.site.urls),
]
