from django.urls import path
from app import views

urlpatterns = [
	path('channel/create/', views.create_channel, name='create_channel'),
	path('channel/<slug>/', views.channel, name='mychannel'),
]