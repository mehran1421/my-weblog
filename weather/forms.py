from django.forms import TextInput,ModelForm
from .models import City

class CityForm(ModelForm):
    class Meta:
        model=City
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'form-control input','placeholder':'نام شهر خود را به لاتین وارد نمایید مانند:Tehran'})}
