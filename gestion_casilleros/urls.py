"""
URL configuration for gestion_casilleros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from casilleros import views
from casilleros.views import (index, send_contact_email, UserCreate, CasilleroList, 
                              ContratoCreate, ContratoUpdate, ContratoList, ContratoDetail)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/casilleros/', CasilleroList.as_view()),
    path('api/contratos/', ContratoCreate.as_view()),
    path('api/contratos/<int:id>/', ContratoUpdate.as_view()),
    path('api/contratos/', ContratoList.as_view(), name='contrato-list'),
    path('api/contratos/<int:id>/', ContratoDetail.as_view(), name='contrato-detail'),
    path('send-email/', send_contact_email, name='send_contact_email'),
    path('api/users/register/', UserCreate.as_view(), name='user-register'),
]

