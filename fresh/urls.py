"""fresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from goods_page.views import search

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'user/',include('user_page.urls')),
    path(r'cart/', include('cart_page.urls')),
    path(r'order/', include('order_page.urls')),
    path(r'goods/', include('goods_page.urls')),
    path(r'tinymce/', include('tinymce.urls')),
    path(r'', include('goods_page.urls', namespace='goods',)),
    path(r'search/', search)
]
