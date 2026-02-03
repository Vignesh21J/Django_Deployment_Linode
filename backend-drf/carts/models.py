from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart({self.user})"
    
    @property
    def subtotal(self):
        subtotal = 0

        # Cart model is there as => FK in => CartItem model. Its instance related_name='items' [Reverse LookUp]. So obj.items
        for item in self.items.all():
            subtotal = subtotal + item.product.price * item.quantity

        return subtotal
    

    @property
    def tax_amount(self):
        tax = 0

        for item in self.items.all():
            tax = tax + item.product.price * item.quantity * item.product.tax_percent/ 100
        return tax
    

    @property
    def grand_total(self):
        grand_total = self.subtotal + self.tax_amount
        return grand_total

    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    @property
    def grand_price(self):
        grand_price = self.product.price * self.quantity
        return grand_price