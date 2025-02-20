from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'city', 'state', 'zip_code', 'country', 'phone', 'delivery_option', 'payment_method']
        widgets = {
            'delivery_option': forms.Select(choices=[
                ('standard', 'Standard Delivery (5-7 business days)'),
                ('express', 'Express Delivery (2-3 business days)'),
            ]),
            'payment_method': forms.Select(choices=[
                ('credit_card', 'Credit Card'),
                ('paypal', 'PayPal'),
                ('cash_on_delivery', 'Cash on Delivery'),
            ]),
        }