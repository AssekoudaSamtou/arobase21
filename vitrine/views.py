from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)

def contact_us(request):
    context = {}
    return render(request, 'contact-us.html', context)