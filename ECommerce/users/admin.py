from django.contrib import admin
from product.models import Product, Order, OrderDetails
from users.models import  Customer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'total_quantity', 'min_quantity', 'max_quantity', 'is_deleted', 'updated_on', 'creation']
    search_fields = ['title', 'product_id', 'description']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id' ,'customer_ref' ,'total_price' ,'payment_status' ,'billing_address' ,'delivery_address' ,'payment_details' ,'additional_data' ,'is_deleted' ,'updated_on' ,'creation']
    search_fields = [ 'order_id']

@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['product_ref', 'order_ref', 'price', 'quantity', 'is_deleted', 'updated_on', 'creation']
    search_fields = ['title', 'description']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'customer_id', 'created_on', 'updated_on', 'is_disabled', 'is_deleted']
    search_fields = ['first_name', 'last_name', 'email']
