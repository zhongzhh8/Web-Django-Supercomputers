"""Web_Django URL Configuration

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
from learn import views as learn_views  # new

urlpatterns = [
    path('', learn_views.home,name='home'),
    path('home', learn_views.home,name='home'),
    path('intro', learn_views.intro,name='intro'),
    path('main', learn_views.main,name='main'),
    path('origin_main', learn_views.origin_main,name='origin_main'),
    path('monitor_data_page/', learn_views.monitor_data_page,name='monitor_data_page'),
    path('RCodePage/', learn_views.R_code_page,name='R_code_page'),
    path('NetDataPage/', learn_views.NetDataPage, name='NetDataPage'),
    path('showdata/', learn_views.showdata, name='showdata'),
    path('add/', learn_views.add, name='add'),
    path('get_heatmap/', learn_views.get_heatmap, name='get_heatmap'),
    path('admin/', admin.site.urls),
]

