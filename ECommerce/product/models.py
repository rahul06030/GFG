from django.db import models
import datetime
from users.models import Customer

class Product(models.Model):
    title = models.TextField(max_length=200, blank=False, null=False)
    product_id = models.TextField(primary_key=True)
    description = models.TextField(blank=False,max_length=1000, null=False)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Seller can decide min and max quantity while purchasing
    min_quantity = models.IntegerField(default=1) 
    max_quantity = models.IntegerField(default=0)

    # seller_ref # TODO link sellers to the product 
    additional_data =models.JSONField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    updated_on = models.DateTimeField(default=datetime.datetime.now())
    creation = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.product_id:
            last_product = Product.objects.order_by('id').last()
            if last_product:
                product_id = 'PRD' + str(int(last_product.product_id[3:]) + 1)
            else:
                product_id = 'PRD1'
            self.product_id = product_id
        super(Product, self).save(*args, **kwargs)

class Order(models.Model):
    order_id = models.TextField(default="", primary_key=True)
    customer_ref = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=25, default="pending")
    billing_address = models.TextField(blank=False,max_length=1000, null=False)
    delivery_address = models.TextField(blank=False,max_length=1000, null=False)
    payment_details = models.JSONField(null=True, blank=True)
    additional_data = models.JSONField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    updated_on = models.DateTimeField(default=datetime.datetime.now())
    creation = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.order_id

    def save(self, *args, **kwargs):
        if not self.order_id:
            last_order = Order.objects.order_by('id').last()
            if last_order:
                order_id = 'ODR' + str(int(last_order.order_id[3:]) + 1)
            else:
                order_id = 'ODR1'
            self.order_id = order_id

        super(Order, self).save(*args, **kwargs)

class OrderDetails(models.Model):
    order_details_id = models.AutoField(primary_key=True, editable=False)

    product_ref = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_ref = models.ForeignKey('Order', related_name='order_details', on_delete=models.CASCADE)
    # seller_ref # TODO
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    updated_on = models.DateTimeField(default=datetime.datetime.now())
    creation = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.order_details_id


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='Product_images/')

#     def __str__(self):
#         return f"Product {self.Product.id} Image"
