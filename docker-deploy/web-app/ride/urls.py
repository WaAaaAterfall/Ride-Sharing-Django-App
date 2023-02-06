from django.urls import path

from . import views
#from .views import OwnerCreateRideView

urlpatterns = [
    path('', views.index, name='index'),
    path('userhome/', views.userhome, name='userhome'),
    path('edit_your_profile', views.edit_profile, name='edit_profile'),
    path('addvehicle/', views.add_vehicle_info, name='addvehicle'),
    path('driverhome/', views.driverhome, name='driverhome'),
    path('newride/', views.create_ride, name='createride'),
    path('your_ride/', views.search_owner_sharer_ride, name='your_ride'),
    path('belong_search/', views.select_belong_ride, name='belong_search'),
    path('user_search_ride/', views.user_search_ride, name = 'user_ride_search'),
    path('ride_search_result/', views.search_open_result, name = 'ride_search_result'),
    path('driver_search/', views.driver_search, name = 'driver_search'),
    path('search_confirm/', views.search_confirm, name = 'search_confirm'),
    path('driver_ride/', views.driver_ride, name = 'driver_ride'),
    path('edit_vehicle/', views.edit_vehicle, name = 'edit_vehicle'),
    path('vehicle_delete/', views.vehicle_delete, name = 'vehicle_delete'),
    path('edit_ride/<int:ride_id>/', views.ride_modify, name = 'edit_ride'),
    path('join_ride/<int:ride_id>/', views.sharer_join, name = 'join_ride'),
    path('leave_ride/<int:ride_id>/', views.sharer_leave, name = 'leave_ride'),
    path('delete_ride/<int:ride_id>/', views.owner_delete, name='owner_delete'),
    path('confirm_ride/<int:ride_id>/', views.confirm_ride, name='confirm_ride'),
    path('complete_ride/<int:ride_id>/', views.complete_ride, name='complete_ride'),
    path('driver_leave/<int:ride_id>/', views.driver_leave, name = 'driver_leave'),
]