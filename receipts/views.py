from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Receipt


# Create your views here.
def show_receipt(request):
    receipt_list = Receipt.objects.all()
    context = {"receipt_list": receipt_list}
    return render(request, "receipts/list.html", context)
