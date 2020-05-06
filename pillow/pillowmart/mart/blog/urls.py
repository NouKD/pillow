from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('<int:categoriearticle_id>/', views.detail, name='detail'),
    #path('<int:categoriearticle_id>/ArchiveA', views.ArchiveA, name='ArchiveA'),
    #path('<int:categoriearticle_id>/ArchiveM', views.ArchiveM, name='ArchiveM'),
    #path('', views.accueil, name='accueil'),
    #path('article/<int:id>', views.lire, name='lire')"""
    path('', views.blog, name="blog"),
    path('<str:filtre>/<int:id>', views.blog, name="blog"),
    path('show/single/<int:id>', views.single_blog, name="single-blog"),
]