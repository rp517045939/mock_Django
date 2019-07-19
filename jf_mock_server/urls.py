"""jf_mock_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from mock import test_mock

urlpatterns = [
    path('admin/', admin.site.urls),
    # ex : /api/post_mock
    # url(r'^api/', include(''))
    url(r'^add_advance/', test_mock.add_advance, name='add_advance'),
    url(r'^api/mock_advance/', test_mock.mock_advance, name='mock_advance')
]
