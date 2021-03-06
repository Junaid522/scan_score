"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import include

from scan_score import views as scan_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', scan_views.home, name='home'),
    url(r'^signup$', scan_views.signup, name='signup'),
    url(r'^login/$', scan_views.login_view, name='login'),
    url(r'^select/$', scan_views.select_test_type, name='select'),
    url(r'^fileupload/', scan_views.model_form_upload, name='fileupload'),
    url(r'^thanks/', scan_views.thanks, name='thanks'),
    url(r'^index/', scan_views.index, name='index'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

]
