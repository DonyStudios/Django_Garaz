from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('garaz1/', views.garaz1, name='garaz1'),
    path('list_ridici/', views.list_ridici, name='list_ridici'),
    path('ridic/<int:id>', views.ridic, name='ridic'),
    path('motor/<int:id>', views.motor, name='motor'),
    path('brzdy/<int:id>', views.brzdy, name='brzdy'),
    path('pneu/<int:id>', views.pneu, name='pneu'),
    path('odpruzeni/<int:id>', views.odpruzeni, name='odpruzeni'),
    path('list_soucastky/', views.list_soucastky, name='list_soucastky'),
    path('vozidlo/<int:id>', views.vozidlo, name='vozidlo'),
]