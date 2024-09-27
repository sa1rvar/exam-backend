"""
URL configuration for project project.

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
from django.urls import path, include, re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project-create/', ProjectCreate().as_view()),
    path('project-list/', ProjectList().as_view()),
    path('project-update/', ProjectUpdate().as_view()),
    path('project-upd-retrieve/<int:pk>', ProjectUpdateRetrieve().as_view()),
    path('project-del/', ProjectDelete().as_view()),
    path('project-get-all', ProjectFoodList.as_view()),
    path('project-create-cat/', ProjectCreateCat().as_view()),
    path('project-list-cat/', ProjectListCat().as_view()),
    path('project-upd-cat/', ProjectUpdateCat().as_view()),
    path('project-del-cat/', ProjectDelCat().as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
