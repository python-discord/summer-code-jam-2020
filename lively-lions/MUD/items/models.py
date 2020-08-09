from django.db import models
# Item Models

# The items can be seperated between magic or physical


class Item_Category(models.Model):
    # Armor? Weapon? Wand?  Consummable
    item_title = models.CharField(max_length=100)
    # magical or physical item?
    type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Item Categories"

    # def __str__(self):
    #     return f"<{self.type}: {self.item_title}>"


class Small_Item(models.Model):
    # Small_Item title which can be obtained from the pk of Item_Category
    item_category = models.ForeignKey(
        'Item_Category',
        default=1,
        verbose_name='Item Name',
        on_delete=models.SET_DEFAULT
        )
    item_name = models.CharField(max_length=30, default='name')
    # The damage output or mana usage
    effect = models.IntegerField()
    # When durability reaches zero item is removed.
    durability = models.IntegerField(default=0)
    # Large Items weight more
    weight = models.IntegerField(default=1)
    # If we have more time, we could lore to some items.
    description = models.CharField(max_length=200, default='None')

    class Meta:
        verbose_name_plural = "Small Items"

    def __str__(self):
        return f"<{self.item_name}>"


class Large_Item(models.Model):
    # Item title which can be obtained from the pk of Item_Category
    item_category = models.ForeignKey(
        'Item_Category',
        default=1,
        verbose_name='Item Name',
        on_delete=models.SET_DEFAULT
        )
    item_name = models.CharField(max_length=30, default='name')
    # The damage output or mana usage
    effect = models.IntegerField()
    # When durability reaches zero item is removed.
    durability = models.IntegerField(default=0)
    # Large Items weight more
    weight = models.IntegerField(default=1)
    # If we have more time, we could lore to some items.
    description = models.CharField(max_length=200, default='None')

    class Meta:
        verbose_name_plural = "Large Items"

    def __str__(self):
        return f"<{self.item_name}>"
