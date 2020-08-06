from django.db import models

# Object Models


class ItemAttribute(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Item Types"

    def __str__(self):
        return f"<{self.stats_type}>"


class Item(models.Model):
    # Item is given name and type
    item_name = models.CharField(max_length=100)
    stats_type = models.ForeignKey(
        ItemAttribute,
        default=1,
        verbose_name="Type",
        on_delete=models.SET_DEFAULT)
    description = models.CharField(max_length=200)
    effect = models.IntegerField()
    durability = models.IntegerField()

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return f"<{self.item_name}: P {self.effect} D {self.durability}>"
