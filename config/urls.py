"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import re_path
from optimizer.views import home, best_team_view, custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Landing page inicial
    path("team/", best_team_view, name="team"),  # Página de otimização
    # Captura qualquer URL que não corresponda às acima e redireciona para 404
    re_path(r'^.*$', custom_404, name="404"),
]

