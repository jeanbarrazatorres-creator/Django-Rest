from django.urls import path 
from .views import ReadInventory, AddtoInventory, UpdateInventory, DeleteInventory 
urlpatterns = [
    path("add/", AddtoInventory.as_view(), name = "add-to-inventory"),
    path("read/", ReadInventory.as_view(), name = "read-inventory"),
    path("update/<int:pk>/", UpdateInventory.as_view(), name = "update-inventory"),
    path("delete/<int:pk>/", DeleteInventory.as_view(), name = "delete-inventory"), 
]