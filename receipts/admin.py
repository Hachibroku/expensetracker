from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt

# Register your models here.
admin.site.register(ExpenseCategory)


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
    )


admin.site.register(Account)


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "owner",
    )


admin.site.register(Receipt)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "vender",
        "total",
        "tax",
        "date",
        "purchaser",
        "category",
        "account",
    )
