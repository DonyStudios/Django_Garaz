from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('garaz1/', views.garaz1, name='garaz1'),
    path('list_ridici/', views.list_ridici, name='list_ridici'),
    path('ridic/<int:id>', views.ridic, name='ridic'),
    path('garaz1/details/<int:id>', views.details, name='details'),
]