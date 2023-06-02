from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm, CategoryForm, AccountForm


# Create your views here.
def redirect_home(request):
    return redirect("home")


@login_required
def show_receipt(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {"receipt_list": receipt_list}
    return render(request, "receipts/list.html", context)


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


@login_required
def show_category(request):
    category_list = ExpenseCategory.objects.filter(owner=request.user)
    context = {"category_list": category_list}
    return render(request, "categories/list.html", context)


@login_required
def show_account(request):
    account_list = Account.objects.filter(owner=request.user)
    context = {"account_list": account_list}
    return render(request, "accounts/list.html", context)
