from django.db import models
from django.contrib.auth.models import User

# User roles
ROLE_CHOICES = [
    ('superadmin', 'SuperAdmin'),
    ('system_admin', 'System Administrator'),
    ('prod_manager', 'Production Manager'),
    ('quality_inspector', 'Quality Inspector'),
    ('assembly_supervisor', 'Assembly Supervisor'),
    ('inventory_manager', 'Inventory Manager'),
    ('finance', 'Finance'),
    ('hr_manager', 'HR Manager'),
    ('receiving_officer', 'Receiving Officer'),
    ('warehouse_controller', 'Warehouse Controller'),
    ('supplier', 'Supplier'),
    ('operator', 'Operator'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AuditTrail(models.Model):
    action = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=255)
    record_id = models.PositiveIntegerField()

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)

class GoodsReceipt(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=True)

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

class QualityControl(models.Model):
    inspect_date = models.DateField()
    results = models.TextField()
    goods_receipt = models.ForeignKey(GoodsReceipt, on_delete=models.CASCADE)

class ProductionOrder(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    scheduled_date = models.DateField()
    status = models.CharField(max_length=50)

class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50)  # e.g., cash, credit
