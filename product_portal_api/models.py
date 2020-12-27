from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=60)
    stock = models.IntegerField()
    selling_price = models.FloatField()
    cost_price = models.FloatField()
    product_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name