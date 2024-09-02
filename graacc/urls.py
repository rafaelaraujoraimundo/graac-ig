"""
URL configuration for graacc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from exames.views import view_padrao

from graacc import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view_padrao, name="index"),
    path('orientacoes_exames', view_padrao, name="exames_orientacoes_fleury")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)