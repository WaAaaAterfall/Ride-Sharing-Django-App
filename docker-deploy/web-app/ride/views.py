from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm#, UserUpdateForm, ProfileUpdateForm, VehicleUpdateForm, RideRequestForm, RideSearchForm
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

@method_decorator(login_required, name='dispatch')
class OwnerCreateRideView(CreateView):
    model = Owner
    fields = ['addr', 'arrive_date', 'passenger_num', 'whether_share', 'max_share_num', 'required_special']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)