from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('mobile-accessories/', mobile_accessories, name='mobile_accessories'),
    path('computer-accessories/', computer_accessories, name='computer_accessories'),
    path('get_cart/', get_cart, name='get_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),

    path('checkout/', checkout, name='checkout'),
]