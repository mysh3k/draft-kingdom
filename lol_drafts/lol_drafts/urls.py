"""lol_drafts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path
from discord_auth.views import *
from champion_api.views import *
#from lol_drafts.discord_auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', AccountLogin.as_view(), name='LoginRequiredRedirect'),
    path('oauth2/login/', AuthDiscord.as_view(), name='AuthDiscord'),
    path('oauth2/login/redirect/', AuthDiscordRedirect.as_view(), name='AuthDiscordRedirect'),
    path('auth/user/', login_required(GetAuthenticatedUser.as_view()), name='GetAuthenticatedUser'),

    path('champions-data/', ChampionsData.as_view(), name='ChampionsData'),
]
