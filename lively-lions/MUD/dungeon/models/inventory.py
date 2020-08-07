from django.db import models
# from django.contrib.auth.models import User


class Inventory(models.Model):
    max_item = models.IntegerField(default=10)
    total_item = models.IntegerField(default=0)
    character = models.ForeignKey('Character', on_delete=models.CASCADE)

    # def get_items(self):
    #     """Get list of item in the inventory
    #     """
    #     pass

    # def drop_item(self, item):
    #     """Drop item from inventory
    #     """
    #     pass

    # def add_item(self, item):
    #     """Add item into inventory
    #     """
    #     pass

    def is_full(self) -> bool:
        """Check if inventory is full or not
        """
        return self.total_item >= self.max_item
