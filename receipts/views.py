from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory, Account


# Create your views here.
@login_required
def show_receipt(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {"receipt_list": receipt_list}
    return render(request, "receipts/list.html", context)


def redirect_home(request):
    return redirect("home")
