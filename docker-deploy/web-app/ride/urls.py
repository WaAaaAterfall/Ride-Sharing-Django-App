from django.urls import path

from . import views
#from .views import OwnerCreateRideView

urlpatterns = [
    path('', views.index, name='index'),
    path('userhome/', views.userhome, name='userhome'),
    # path('newride/', OwnerCreateRideView.as_view(), name='create_ide'),
    path('newride/', views.createride, name='createride'),

    path('rideinfo/', views.rideinfo, name='rideinfo'),
    path('addvehicle/', views.add_vehicle_info, name='addvehicle'),
    path('driverhome/', views.driverhome, name='driverhome'),
    
]