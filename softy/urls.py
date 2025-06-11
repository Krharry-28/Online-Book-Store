from django.contrib import admin
from django.urls import path
from softy import views 
from softwr import settings 

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('sign_up',views.sign_up, name="sign_up"),
    
    

#another one

    path('about',views.about,name='about'),
    path('aabook', views.aabook, name='aabook'),
    path("contact", views.contact, name='contact'), 
    path('services',views.services,name='services'),
    path('index',views.index,name='index'),
    path('home',views.home,name='home'),
    path('cover',views.cover,name='cover'),
    path('list',views.list , name='list'),
    path('aabook_form/', views.aabook_form, name='aabook_form'),
    path('ambook/', views.AManageBook.as_view(), name='ambook'),
    path('adbook/<int:pk>', views.ADeleteBook.as_view(), name='adbook'),
    path('avbook/<int:pk>', views.AViewBook.as_view(), name='avbook'),
    path('albook/', views.ABookListView.as_view(), name='albook'),
    path('ambook/', views.AManageBook.as_view(), name='ambook'),
    path('albook0/', views.ABookListView0.as_view(), name='albook0'),
    path('albook1/', views.ABookListView1.as_view(), name='albook1'),
    path('albook2/', views.ABookListView2.as_view(), name='albook2'),
    path('albook3/', views.ABookListView3.as_view(), name='albook3'),
    path('albook4/', views.ABookListView4.as_view(), name='albook4'),
    path('albook5/',views.ABookListView5.as_view(),name='albook5'),
    path('albook6/',views.ABookListView6.as_view(),name='albook6'), 
    path('albook7/',views.ABookListView7.as_view(),name='albook7'),
    path('albook8/',views.ABookListView8.as_view(),name='albook8'),
    path('avbook/<int:pk>', views.AViewBook.as_view(), name='avbook'),
]

