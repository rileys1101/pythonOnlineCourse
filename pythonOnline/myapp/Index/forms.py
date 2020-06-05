from django.forms import ModelForm
from .models import UserForm

class DBFrom(ModelForm):
    class Meta:
        model = UserForm
        fields =['name','address',]