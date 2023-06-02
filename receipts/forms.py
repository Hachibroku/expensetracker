from django import forms
from django.forms import ModelForm
from receipts.models import Receipt


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]


class CategoryForm(forms.Form):
    pass


class AccountForm(forms.Form):
    pass
