"""aaoSeekheinBackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from signin.views import user_signin
from asToken.views import get_token
from asUser.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aaoseekhein/v1/signin', user_signin),
    path('aaoseekhein/v1/gettoken', get_token),
    path('aaoseekhein/v1/user', UserViewSet.as_view({'get': 'list', 'patch': 'partial_update'})),
    path('aaoseekhein/v1/user/<int:pk>', UserViewSet.as_view({'get': 'list', 'patch': 'partial_update'})),

]
