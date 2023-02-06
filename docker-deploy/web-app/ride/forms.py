from django import forms
from .models import DriverVehicle, RideOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class RideCreateForm(forms.ModelForm):
    vehicle_type = forms.ChoiceField(label='Vehicle Type', choices=(
        ("None", "None"), ("Sedan", "Sedan"), ("SUV", "SUV"), ("Hatchback", "Hatchback")), required=False)

    class Meta:
        model = RideOrder
        fields = ['destination', 'arrive_date', 'passenger_num',
                  'sharable', 'vehicle_type', 'special_request']


class RideSearchForm(forms.Form):
    destination = forms.CharField()
    earliest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])
    latest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])
    passenger_num = forms.IntegerField()

class BelongSearchForm(forms.Form):
    destination = forms.CharField()
    earliest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])
    latest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])


class DriverSearchForm(forms.Form):
    destination = forms.CharField()
    earliest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])
    latest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])


class DriverSearchConfirmForm(forms.Form):
    destination = forms.CharField()
    earliest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])
    latest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'])


class VehicleForm(forms.ModelForm):
    plate = forms.CharField(label='License Plate No.', required=True)
    vehicle_type = forms.ChoiceField(label='Vehicle Type', choices=(
        ("Sedan", "Sedan"), ("SUV", "SUV"), ("Hatchback", "Hatchback")))
    special_info = forms.CharField(label='Special Info', required=False)

    class Meta:
        model = DriverVehicle
        fields = ['plate', 'capacity', 'vehicle_type', 'special_info']
