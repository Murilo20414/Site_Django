from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/edit/<slug:slug>/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/', views.BlogDetailView.as_view(), name='post_detail'),

]