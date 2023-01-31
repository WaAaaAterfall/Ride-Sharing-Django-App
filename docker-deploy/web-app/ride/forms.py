from django import forms
from .models import User, Vehicle, Owner
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100,required=True)
    #is_driver = forms.BooleanField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class UserEditForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100,required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class RideCreateForm(forms.ModelForm):
    addr = forms.CharField()
    arrive_date = forms.DateField()
    passenger_num = forms.IntegerField()
    whether_share = forms.BooleanField()
    max_share_num = forms.IntegerField()
    required_special = forms.CharField()
    
    class Meta:
        model = Owner
        fields = ['addr', 'arrive_date', 'passenger_num', 'whether_share', 'max_share_num', 'required_special']


class VehicleForm(forms.ModelForm):
    type = forms.CharField()
    plate = forms.CharField()
    capacity = forms.IntegerField()
    comment = forms.CharField()
    class Meta:
        model = Vehicle 
        fields = ['type', 'plate', 'capacity', 'comment']

# class DriverRegistrationForm(forms.Form):
#     DOB = forms.DateField(label='Date of Birth',required=True,
#                                 input_formats = ['%Y-%m-%d'],
#                                 widget=DateInput(format='%Y-%m-%d'))
#     licenseNumber = forms.CharField(label='License No.',required=True)
#     VehicleType = forms.ChoiceField(label='Vehicle Type',choices=(("Sedan", "Sedan"),("SUV", "SUV")))
#     brand = forms.CharField(label='Vehicle Brand',required=True)
#     model = forms.CharField(label='Vehicle Model',required=True)
#     plateNum = forms.CharField(label='Plate No.',required=True)
#     max_pnum = forms.IntegerField(label='Max Passenger No.',required=True)
#     special_info = forms.CharField(label='Special Info',required=False)
    
#     class Meta:
#         model = Driver
#         fields = ['DOB','licenseNum','Vtype','brand','model','plateNum','max_pnum','special_info']