from django.urls import path
from receipts.views import (
    show_receipt,
    create_receipt,
    show_category,
    show_account,
    create_category,
)

urlpatterns = [
    path("", show_receipt, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", show_category, name="category_list"),
    path("accounts/", show_account, name="account_list"),
    path("categories/create/", create_category, name="create_category"),
]
