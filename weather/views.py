import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

# Create your views here.

#https://openweathermap.org/current
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperials&appid=bd4331ae65a371e51693fb6f1b43fc28'

    err_msg=''
    message=''
    message_class=''

    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            new_city=form.cleaned_data['name']
            existing_city_count=City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod']==200:
                    form.save()
                else:
                    err_msg='این شهر وجود ندارد'
            else:
                err_msg='این شهر از قبل وجود دارد'


        if err_msg:
            message=err_msg
            message_class='is_danger'
        else:
            message='این شهر با موفقیت وارد شد'
            message_class='is-success'

    form=CityForm()

    cities=City.objects.all().order_by('name')
    cities_whether=[]


    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_weather={
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        cities_whether.append(city_weather)

    context={
        'city_weather':cities_whether,
        'form':form,
        'message':message,
        'message_class':message_class,
    }

    return render(request,'weather/weather.html',context)

def delete_city(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('weather:weather_home')