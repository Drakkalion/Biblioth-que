from django.contrib import admin
from django.urls import path
from . import views

app_name = "elements"

urlpatterns = [
    path('',views.elements_view,name="elements"),
    path('films/',views.film_view,name="film"),
    path('series/',views.series_view,name="serie"),
    path('disney/',views.disney_view,name="disney"),
    path('favori/',views.favori_view,name="favori"),
    path('decouvrir/',views.decouvrir_view,name="decouvrir"),
    path('revoir/',views.revoir_view,name="revoir"),
    path('acheter/',views.acheter_view,name="acheter"),
    path('creer/',views.creer_view,name="creer"),
    path('search/',views.search_view,name="search"),
    path('update/',views.update_view,name="update"),
    # path('update2/<int:idelement>/',views.update2_view,name='update2'),
    path('update2',views.update2_view,name='update2'),
    path('remerciements/',views.remerciements_view,name='remerciements'),
    # Il faut mettre la version slug à la fin, sinon django va croire que c'est l'url slug qu'on veut utiliser
    path('<int:idelement>/',views.details_view,name='detail')
] 
