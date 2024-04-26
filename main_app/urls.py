from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
  path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('songs/', views.SongList.as_view(), name='songs_index'),
  path('songs/<int:pk>/', views.SongDetail.as_view(), name='songs_detail'),
  path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
  path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
]