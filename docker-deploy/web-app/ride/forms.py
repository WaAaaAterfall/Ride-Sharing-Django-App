from django import forms
from .models import DriverVehicle, RideOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100,required=True)
    #is_driver = forms.BooleanField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100,required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class RideCreateForm(forms.ModelForm):

    class Meta:
        model = RideOrder
        fields = ['destination', 'arrive_date', 'passenger_num', 'sharable', 'max_share_num', 'required_special']

class RideSearchForm(forms.Form):
    destination = forms.CharField()
    earliest_time = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'])
    latest_time = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'])
    passenger_num = forms.IntegerField()

class VehicleForm(forms.ModelForm):
    plate = forms.CharField(label='License Plate No.',required=True)
    Vtype = forms.ChoiceField(label='Vehicle Type',choices=(("Sedan", "Sedan"),("SUV", "SUV")))
    brand = forms.CharField(label='Vehicle Brand',required=True)
    special_info = forms.CharField(label='Special Info',required=False)

    class Meta:
        model = DriverVehicle
        fields = ['plate', 'capacity', 'Vtype', 'brand', 'special_info']