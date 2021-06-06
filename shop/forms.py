from django import forms


class BuyProductFrom(forms.Form):
    quantity = forms.TypedChoiceField(choices=[(1, '1'), (2, '2')], coerce=int)
