from django.urls import path

from . import views
#from .views import OwnerCreateRideView

urlpatterns = [
    path('', views.index, name='index'),
    path('userhome/', views.userhome, name='userhome'),
    path('edit_your_profile', views.edit_profile, name='edit_profile'),
    path('addvehicle/', views.add_vehicle_info, name='addvehicle'),
    path('newride/', views.create_ride, name='createride'),
    path('rideinfo/', views.rideinfo, name='rideinfo'),
    path('your_ride/', views.search_owner_sharer_ride, name='your_ride'),
    path('complete_ride/<int:ride_id>', views.complete_ride, name='complete_ride'),
    path('user_search_ride/', views.user_search_ride, name = 'user_ride_search'),
    path('ride_search_result/', views.search_open_result, name = 'ride_search_result'),
    path('edit_ride/<int:ride_id>/', views.ride_modify, name = 'edit_ride'),
    path('join_ride/<int:ride_id>/', views.sharer_join, name = 'join_ride')
]