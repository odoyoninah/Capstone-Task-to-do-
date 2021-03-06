from django.conf import settings
from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')), 
    path('createtask/', views.createtask, name='createtask'),
    path('task/', views.task, name='task'),
    path('search/', views.search_task, name='search_task'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
