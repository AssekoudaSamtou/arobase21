from django.urls import path, include

from vitrine.views import home, contact_us

urlpatterns = [
    path('', home, name='home'),
    path('contact-us', contact_us, name='contact-us'),
]