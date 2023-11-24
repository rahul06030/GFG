from django.db import models
import hashlib


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True,  null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    customer_id = models.AutoField(primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_disabled = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    additional_data = models.JSONField(null=True, blank=True)
    password = models.CharField(max_length=128, default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.customer_id})"

    def set_password(self, raw_password):
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password):
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()
    