from django.contrib import admin
from django.urls import path , include
from Home import views

admin.site.site_header = "Welcome Mr. Administrator"
admin.site.site_title = "This is Admin zone"
admin.site.index_title = "Databases"
urlpatterns =[
    path('', views.home , name = 'home'),
   
]
 