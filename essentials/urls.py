from django.urls import path
from .views import *
from django.views.generic import TemplateView

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
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('update-cart-quantity/', update_cart_quantity, name='update_cart_quantity'),
    path('order-confirmation/<str:order_number>/', order_confirmation, name='order_confirmation'),

    path('privacy-policy/', privacy_policy_view, name='privacy_policy'),
    path('shipping-policy/', shipping_policy_view, name='shipping_policy'),


    path('warranty/', warranty_info, name='warranty_info'),
    path('faq/', faq_page, name='faq_page'),
    path('terms/', terms_page, name='terms_page'),


]

