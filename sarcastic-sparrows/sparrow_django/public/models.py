from django.db import models


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    ticker_symbol = models.CharField(max_length=5)
    open = models.DecimalField(max_digits=20, decimal_places=5)
    high = models.DecimalField(max_digits=20, decimal_places=5)
    low = models.DecimalField(max_digits=20, decimal_places=5)
    close = models.DecimalField(max_digits=20, decimal_places=5)
    volume = models.IntegerField()

    def __str__(self):
        return "Name: <%r> Date: <%r> High: <%.4f> Low: <%.4f>" % (
            self.ticker_symbol,
            str(self.date),
            self.high,
            self.low,
        )


class Buy(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    ticker_symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    volume = models.IntegerField()

    def __str__(self):
        return f"Name: {self.ticker_symbol} Date: {str(self.date)} Size: {self.volume}"


class Sell(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    ticker_symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    volume = models.IntegerField()

    def __str__(self):
        return f"Name: {self.ticker_symbol} Date: {str(self.date)} Size: {self.volume}"
