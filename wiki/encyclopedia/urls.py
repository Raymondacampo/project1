from django.urls import path

from . import views

# app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry, name="entry"),
    path('search/', views.search, name='search'),
    path('new', views.new, name='new'),
    path('edit/<str:doc>', views.edit, name='edit')
]
