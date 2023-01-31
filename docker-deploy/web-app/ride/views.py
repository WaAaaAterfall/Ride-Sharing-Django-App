from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, VehicleForm, RideCreateForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Owner


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
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
    return render(request, 'ride/userhome.html')

def rideinfo(request):
    data = Owner.objects.all()

    return render(request, 'ride/rideinfo.html', {'data': data})

# @method_decorator(login_required, name='dispatch')
# class OwnerCreateRideView(CreateView):
#     model = Owner
#     fields = ['addr', 'arrive_date', 'passenger_num', 'whether_share', 'max_share_num', 'required_special']

#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super().form_valid(form)

@login_required
def createride(request):
    if request.method == 'POST':
        form = RideCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your ride information has been added')
            return redirect('rideinfo')
    else:
        form = RideCreateForm()

    context = {
        'form' : form
    }
    
    return render(request, 'ride/newride.html', context)

@login_required
def addvehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your vehicle information has been updated')
            return redirect('userhome')
    else:
        form = VehicleForm()

    context = {
        'form' : form
    }
    
    return render(request, 'ride/addvehicle.html', context)

def forms_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

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