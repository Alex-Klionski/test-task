from django import forms
from django.forms import ModelChoiceField

from .models import UserProfile, Device


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'devices']


class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = '__all__'
        exclude = ['date', 'used_by']


class GiveOutForm(forms.ModelForm):
    device = ModelChoiceField(queryset=Device.objects.filter(used_by=None))

    class Meta:
        model = Device
        fields = ['used_by', 'device']
