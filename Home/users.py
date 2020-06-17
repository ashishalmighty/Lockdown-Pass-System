from django import forms
from .models import UserData, CitizenRequest, CorporateRequest


class Login(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'email', 'password', 'aadhaar', 'usertype']


class CitRequest(forms.ModelForm):
    class Meta:
        model = CitizenRequest
        fields = ['aadhaar', 'req_date', 'req_time', 'req_duration']


class CorRequest(forms.ModelForm):
    class Meta:
        model = CorporateRequest
        fields = ['aadhaar', 'organization_name', 'cin_no', 'industry_type', 'num_requested',
                  'req_date', 'req_time', 'req_duration']