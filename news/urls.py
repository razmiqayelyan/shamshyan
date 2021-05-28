from django.urls import path, include
from .views import *
urlpatterns = [
	path('', index, name='index'),
	path('search/', search, name='search'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('detail/<int:pk>/<str:slug>/',NewsDetail, name='detail'),
	path('category/<slug:slug>/', kategorya, name='kategorya'),
	path('delete/onlybyrazo/<int:pk>/', delete, name='delete'),
	path('reset/', reset, name='reset'),
	path('reset/confirm/', resetconf , name='resetconf'),
	path('email/confirm/', emailconf, name='emailconf'),

]