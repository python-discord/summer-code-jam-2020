from django.db import models


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticker_symbol = models.CharField(max_length=4)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
