from django.contrib import admin
from django.urls import path , include
from Home import views

admin.site.site_header = "Welcome Mr. Administrator"
admin.site.site_title = "This is Admin zone"
admin.site.index_title = "Databases"
urlpatterns =[
    path('', views.home , name = 'home'),
    path('Brain', views.brain , name = 'brain'),
    path('Beginner', views.beginner , name = 'beginner'),
    path('Brute', views.brute , name = 'brute'),
    path('Greed', views.greed , name = 'greed'),
    path('Sub', views.sub , name = 'sub'),
    path('Implement', views.implement , name = 'implement'),
    path('Sort', views.sort , name = 'sort'),
    path('Binary', views.binary , name = 'binary'),
    path('Pointer', views.pointer , name = 'pointer'),
    path('Hash', views.hash , name = 'hash'),
    path('Pair', views.pair , name = 'pair'),
    path('Dpstand', views.dpstand , name = 'dpstand'),
    path('Dp', views.dp , name = 'dp'),
    path('Tree', views.tree , name = 'tree'),
    path('Graph', views.graph , name = 'graph'),
    path('DSU', views.dsu , name = 'dsu'),
    path('Segtree', views.segtree , name = 'segtree'),
]
 