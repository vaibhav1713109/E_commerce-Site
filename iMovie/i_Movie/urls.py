from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>', views.Details, name='details'),
    path('search/', views.search, name='search'),
    path('action/', views.Action, name='action'),
    path('adventure/', views.Adventure, name='adventure'),
    path('animated/', views.Animated, name='animated'),
    path('comedy/', views.Comedy, name='comedy'),
    path('crime/', views.Crime, name='crime'),
    path('horror/', views.Horror, name='horror'),
    path('fantasy/', views.Fantasy, name='fantasy'),
    path('sci-fi/', views.Sci_Fi, name='sci-fi'),
    path('romentic/', views.Romentic, name='romentic'),
]