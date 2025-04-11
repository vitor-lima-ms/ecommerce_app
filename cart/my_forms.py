from django import forms

PRODUCT_QTD_OPT = []
for i in range(1, 201):
    PRODUCT_QTD_OPT.append((i, str(i)))

class AddCartForm(forms.Form):
    qtd = forms.TypedChoiceField(choices=PRODUCT_QTD_OPT, coerce=int)
    att = forms.BooleanField(required=False, widget=forms.HiddenInput)