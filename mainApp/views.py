from django.shortcuts import render

# Create your views here.


def index (request):
    return render(request, 'mainApp/homePage.html')


def contact (request):
    return render(request, 'mainApp/basic.html', {'values': [' любая инфа ', "номер мобильный и тд 49159735870957132051"]})
