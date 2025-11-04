from django.db import models
from django.contrib.auth.models import User
from shop.models import products


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        else:
            return f"Cart for session {self.session_key}"

    @property
    def total_items(self):
        return sum(item.quantity for item in self.cartitem_set.all())

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cartitem_set.all())

    @property
    def total_discount(self):
        return sum(item.total_discount for item in self.cartitem_set.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.discountprice

    @property
    def total_original_price(self):
        if self.product.originalprice:
            return self.quantity * self.product.originalprice
        return 0

    @property
    def total_discount(self):
        if self.product.originalprice:
            return self.total_original_price - self.total_price
        return 0

    @property
    def savings_percentage(self):
        if self.product.originalprice and self.product.originalprice > 0:
            return round((self.total_discount / self.total_original_price) * 100, 2)
        return 0