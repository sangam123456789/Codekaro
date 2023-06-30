from django.contrib import admin
from django.urls import path , include
from Home import views

admin.site.site_header = "Welcome Mr. Administrator"
admin.site.site_title = "This is Admin zone"
admin.site.index_title = "Databases"
urlpatterns =[
    path('', views.home , name = 'home'),
    path('Brain', views.brainf , name = 'brainf'),
    path('Beginner', views.beginner , name = 'beginnerf'),
    path('Brute', views.brutef , name = 'brutef'),
    path('Greed', views.greedf , name = 'greedf'),
    path('Sub', views.subf , name = 'subf'),
    path('Implement', views.implementf , name = 'implementf'),
    path('Sort', views.sortf , name = 'sortf'),
    path('Binary', views.binaryf , name = 'binaryf'),
    path('Pointer', views.pointerf , name = 'pointerf'),
    path('Hash', views.hashf , name = 'hashf'),
    path('Pair', views.pairf , name = 'pairf'),
    path('Dpstand', views.dpstandf , name = 'dpstandf'),
    path('Dp', views.dpf , name = 'dpf'),
    path('Tree', views.treef , name = 'treef'),
    path('Graph', views.graphf , name = 'graphf'),
    path('DSU', views.dsuf , name = 'dsuf'),
    path('Segtree', views.segtreef , name = 'segtreef'),
]
 