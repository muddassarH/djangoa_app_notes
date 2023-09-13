from django.urls import path
from .views import HomeView, ArticleView , AddPostView ,UpdatePostView ,SearchView , DeletePostView ,UserRegisterView
from . import views
urlpatterns = [
    # path('a/',views.home),
    path('article/<int:pk>/', ArticleView.as_view(), name='article-detail'),
    path('',  HomeView.as_view(), name='home'),
    path('add_notes/', AddPostView.as_view(), name="add_post"),
    path('search/', views.SearchView.as_view(), name='search_results'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name="edit_notes"),
    path('article/remove/<int:pk>/', DeletePostView.as_view(), name="delete_note"),
    path('register/', UserRegisterView.as_view(), name="register"),


]
