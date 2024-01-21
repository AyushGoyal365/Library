"""Library URL Configuration

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
from django.urls import path
from signup import views
from django.conf import settings
from django.conf.urls.static import static
from signup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.AOA,name='AOA'),
    path('AOA/',views.AOA,name='AoA'),
    path('sign-up/',views.authorsign_up,name='authorsignup'),
    path('home/',views.authorhome,name='authorhome'),
    path('sign-in/',views.authorsign_in,name='authorsignin'),
    path('asign-in/',views.adminsign_in,name='adminsignin'),
    path('ahome/',views.adminhome,name='adminhome'),
    path('myaccount/',views.authoraccount,name='authoraccount'),
    path('add-new-book/',views.addnewbook,name='addnewbook'),
    path('your-books/',views.yourbook,name='yourbooks'),
    path('all-books/',views.allbook,name='allbooks'),
    path('adaccount/',views.adminaccount,name='adminaccount'),
    path('all-authors/',views.allauthors,name='allauthors'),
    path('aall-books/',views.adminallbooks,name='aallbooks'),
    path('author/<str:username>/', views.author_detail, name='author_detail'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)