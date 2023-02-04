from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, VehicleForm, RideCreateForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import RideOrder, Driver


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save() 
            messages.success(request, f'You account have already created. You can login now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'ride/register.html', {'form': form})

def login(request):
    return render(request, 'ride/login.html')

def home(request):
    return render(request, 'ride/home.html')

def userhome(request):
    vehicle = Driver.objects.get(pk=request.user.id)
    return render(request, 'ride/userhome.html', {'vehicle': vehicle})
    
def driverhome(request):
    vehicle = Driver.objects.get(pk=request.user.id)
    return render(request, 'ride/driverhome.html', {'vehicle': vehicle})

def rideinfo(request):
    data = RideOrder.objects.filter(owner_id=request.user.id)

    return render(request, 'ride/rideinfo.html', {'data': data})

@login_required
def createride(request):
    ride = RideOrder()
    if request.method == 'POST':
        form = RideCreateForm(request.POST)
        if form.is_valid():
            ride.addr = form.cleaned_data['addr']
            ride.arrive_date = form.cleaned_data['arrive_date']
            ride.owner = request.user
            ride.passenger_num = form.cleaned_data['passenger_num']
            ride.required_special = form.cleaned_data['required_special']
            ride.max_share_num = form.cleaned_data['max_share_num']
            ride.sharable = form.cleaned_data['sharable']
            ride.status = 'open'
            ride.save()
            messages.success(request, f'Your ride information has been added')
            return redirect('rideinfo')
    else:
        form = RideCreateForm()

    return render(request, 'ride/newride.html', {'form' : form})

@login_required
def add_vehicle_info(request):
    vehicle = Driver()
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle.driver = request.user
            vehicle.plate = form.cleaned_data['plate']
            vehicle.Vtype = form.cleaned_data['Vtype']
            vehicle.brand = form.cleaned_data['brand']
            vehicle.special_info = form.cleaned_data['special_info']
            vehicle.save()
            messages.success(request, f'Your vehicle information has been updated')
            return redirect('driverhome')
    else:
        form = VehicleForm()

    return render(request, 'ride/addvehicle.html', {'form' : form})

# def contact(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = ContactForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # ...
#             return HttpResponseRedirect('/thanks/') # Redirect after POST
#     else:
#         form = ContactForm() # An unbound form

#     return render(request, 'contact.html', {
#         'form': form,
#     })