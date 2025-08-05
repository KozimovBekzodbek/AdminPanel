from django import forms
from restoran.models import Order

class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

