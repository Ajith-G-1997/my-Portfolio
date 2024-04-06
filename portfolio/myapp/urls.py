from django.urls import path
from . import views

urlpatterns = [
    path('', views.Banner,name='home-page'),
    path('about/',views.Education,name='about'),
    path('portfolio/',views.Portfolio,name='portfolio'),
    path('service/',views.Service,name='service'),
    path('likes/',views.Likes,name='likes'),
    path('food-detail/',views.Food_Detail,name='food-detail'),
    path('games-detail/',views.Game_Detail,name='games-detail'),
    path('football-detail/',views.Football_Detail,name='football-detail'),
    path('blog-list', views.blog_list, name='blog-list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/new/', views.blog_create, name='blog_create'),
    path('blog/<int:pk>/edit/', views.blog_update, name='blog_update'),
    path('blog/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('contact',views.contact,name='contact')

]