from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserEditForm, VehicleForm, RideCreateForm, RideSearchForm
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import RideOrder, DriverVehicle
#from django.db.models import Q


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
    if request.user.is_authenticated:
        try:
            vehicle = DriverVehicle.objects.get(pk=request.user.id)
        except DriverVehicle.DoesNotExist:
            vehicle = None
        return render(request, 'ride/userhome.html', {'vehicle': vehicle})
    else:
        messages.warning(request, f'You are logged out. Please log in first')
        return redirect('login')

@login_required()
def driverhome(request):
    vehicle = DriverVehicle.objects.get(pk=request.user.id)
    return render(request, 'ride/driverhome.html', {'vehicle': vehicle})

@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save() 
            messages.success(request, f'You profile have been modified.')
            return redirect('userhome')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'ride/edit_profile.html', {'form': form})


@login_required()
def rideinfo(request):
    data = RideOrder.objects.filter(owner_id=request.user.id)

    return render(request, 'ride/rideinfo.html', {'data': data})

@login_required
def create_ride(request):
    ride = RideOrder()
    if request.method == 'POST':
        form = RideCreateForm(request.POST)
        if form.is_valid():
            ride.destination = form.cleaned_data['destination']
            ride.arrive_date = form.cleaned_data['arrive_date']
            ride.owner = request.user
            ride.passenger_num = form.cleaned_data['passenger_num']
            ride.required_special = form.cleaned_data['required_special']
            ride.max_share_num = form.cleaned_data['max_share_num']
            ride.sharable = form.cleaned_data['sharable']
            ride.status = 'open'
            ride.save()
            messages.success(request, f'Your ride information has been added')
            return redirect('your_ride')
    else:
        form = RideCreateForm()

    return render(request, 'ride/newride.html', {'form' : form})

@login_required()
def user_search_ride(request):
     if(request.method == 'POST'):
         form = RideSearchForm(request.POST)
         #ride = None
         if form.is_valid():
             dest = form.cleaned_data['destination']
             earliest_time =  form.cleaned_data['earliest_time']
             latest_time = form.cleaned_data['latest_time']
             passenger_num = form.cleaned_data['passenger_num']
             ride = RideOrder.objects.filter(destination = dest, 
                                             status = 'open', 
                                             sharable = True, 
                                             arrive_date__range=(earliest_time,latest_time),
                                             passenger_num__gte = passenger_num)
             return render(request, 'ride/ride_search_result.html', {'rides':ride})
     else :
         form = RideSearchForm()
         return render(request, 'ride/user_search.html', {'form':form})
# def user_search_ride(request):
#     if(request.method == 'POST'):
#         form = RideSearchForm(request.POST)
#         if form.is_valid():
#             request.session['destination'] = request.POST['destination']
#             request.session['earliest_time'] = request.POST['earliest_time']
#             request.session['latest_time'] = request.POST['latest_time']
#             request.session['passenger_num'] = request.POST['passenger_num']
#             return redirect('ride_search_result')
#     else :
#         form = RideSearchForm()
#     return render(request, 'ride/user_search.html', {'form':form})

@login_required()
def search_open_result(request):
    dest = request.session.get('destination')
    earliest_time = request.session.get('earliest_time')
    latest_time = request.session.get('latest_time')
    passenger_num = request.session.get('passenger_num')
    rides = RideOrder.objects.filter(destination = dest, 
                                    status = 'open', 
                                    sharable = True, 
                                    arrive_date__range=(earliest_time,latest_time),
                                    passenger_num__gte = passenger_num)
    return render(request, 'ride/ride_search_result.html', {'rides':rides})

@login_required()
def ride_modify(request, ride_id):
    if request.method == 'POST':
        ride = RideOrder.objects.filter(pk=ride_id).first()
        if ride.status == 'open':
            form = RideCreateForm(request.POST, instance=ride)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your ride has been updated')
                return redirect('your_ride')
        else:
            messages.warning(request, f'Your ride is not open any more, so you cannot edit it')
            return redirect('your_ride')       
    else:
        ride = RideOrder.objects.filter(pk=ride_id).first()
        form = RideCreateForm(instance=ride)

    return render(request, 'ride/edit_ride.html', {'form':form})

@login_required()
def search_owner_sharer_ride(request):
    try:
        owner_ride = RideOrder.objects.filter(owner = request.user.id)
    except RideOrder.DoesNotExist:
        owner_ride = None

    try:
        sharer_ride = RideOrder.objects.filter(sharer=request.user.id)
    except RideOrder.DoesNotExist:
        sharer_ride = None

    context = {'owner_ride': owner_ride, 'sharer_ride': sharer_ride}
    return render(request, 'ride/your_ride.html', context)

@login_required()
def driver_search(request):
    if(request.method == 'POST'):
        form = RideSearchForm(request.POST)
        #ride = None
        if form.is_valid():
            dest = form.cleaned_data['destination']
            earliest_time =  form.cleaned_data['earliest_time']
            latest_time = form.cleaned_data['latest_time']
            passenger_num = form.cleaned_data['passenger_num']
            ride = RideOrder.objects.filter(destination = dest, 
                                            status = 'open', 
                                            sharable = True, 
                                            arrive_date__range=(earliest_time,latest_time),
                                            passenger_num__gte = passenger_num)
            return render(request, 'ride/ride_search_result.html', {'rides':ride})
    else :
        form = RideSearchForm()
        return render(request, 'ride/user_search.html', {'form':form})
    
@login_required()
def driver_ride(request):
    

@login_required()
def sharer_join(request, ride_id):
    ride = RideOrder.objects.filter(pk=ride_id).first()
    if request.user in ride.sharer.all():
        messages.warning(request, f'Your already joined the ride as a sharer')
        return redirect('your_ride')
    ride.sharer.add(request.user)
    ride.save()
    messages.success(request, f'You have joined the ride')
    return redirect('your_ride')

@login_required()
def sharer_leave(request, ride_id):
    ride = RideOrder.objects.filter(pk=ride_id).first()
    ride.sharer.remove(request.user)
    ride.save()
    messages.success(request, f'You have left the ride')
    return redirect('your_ride')

@login_required()
def complete_ride(request, ride_id):
    ride = RideOrder.objects.filter(pk=ride_id).first()
    ride.status='completed'
    ride.save()
    messages.success(request, f'You have completed the ride')
    return redirect('your_ride')

@login_required()
def owner_delete(request, ride_id):
    ride = RideOrder.objects.filter(pk=ride_id).first()
    ride.delete()
    messages.success(request, f'You have deleted the ride')
    return redirect('your_ride')

@login_required
def add_vehicle_info(request):
    vehicle = DriverVehicle()
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
