from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm


# Create your views here.
@login_required
def show_receipt(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {"receipt_list": receipt_list}
    return render(request, "receipts/list.html", context)


def redirect_home(request):
    return redirect("home")


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {"form": form}
    return render(request, "receipts/create.html", context)
