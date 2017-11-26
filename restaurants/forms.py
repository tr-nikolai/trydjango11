from django import forms
from .models import Restaurant


class RestaurantCreateForms(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category =  forms.CharField(required=False)


class RestaurantCreateModelForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'category']