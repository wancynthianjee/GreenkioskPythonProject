from django.urls import path
from .views import CustomerDetailView, CustomerListView


urlpatters =[
    path("customers/", CustomerListView.as_view, name="customer_list_view"),
    path("customers/<int:id>/",CustomerDetailView.as_view,name="customer_detail_view"),
]
