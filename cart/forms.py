from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]
class CartForm(forms.Form):
    num = forms.TypedChoiceField(label="購買數量", choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
