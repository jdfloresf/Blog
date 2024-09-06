#
from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path('perfil/', views.UserPageListView.as_view(), name='perfil'), 
    path('agregar-favorito/<pk>/', views.AddFavoritoView.as_view(), name='add-fav'), 
    path('eliminar-favorito/<pk>/', views.FavoritesDeleteView.as_view(), name='delete-fav'), 
]