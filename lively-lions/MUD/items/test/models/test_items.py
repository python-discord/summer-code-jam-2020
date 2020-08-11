from django.test import TestCase
import pytest
from items.models import Item_Category, Small_Item, Large_Item

# Create your tests here.


@pytest.mark.django_db
class CreateItem(TestCase):

    @classmethod
    def setUp(self):
        # sets up the categories
        self.armor_physical = Item_Category.objects.create(
                                item_title='Armor',
                                type='Physical'
                                )
        self.small_buckler = Small_Item.objects.create(
                                item_category=self.armor_physical,
                                item_name='Small Buckeler',
                                effect=5,
                                durability=7,
                                weight=1,
                                description='Small shield for defending.'
                                )
        self.large_shield = Large_Item.objects.create(
                                item_category=self.armor_physical,
                                item_name='Large Shield',
                                effect=7,
                                durability=12,
                                weight=2,
                                description='Large Shield for defending.'
                                )

    def test_create_item_category(self):
        assert Item_Category.objects.count() == 1, 'Should be equal'
        assert Item_Category.objects.get(pk=1).item_title == self.armor_physical.item_title, "Should be equal"

    def test_create_small_item(self):
        assert Small_Item.objects.count() == 1, 'Should be equal'
        assert Small_Item.objects.get(pk=1) == self.small_buckler, "Should be equal"
        assert Small_Item.objects.get(pk=1).item_name == self.small_buckler.item_name, "Should be equal"
        assert Small_Item.objects.get(pk=1).effect == self.small_buckler.effect, "Should be equal"
        assert Small_Item.objects.get(pk=1).durability == self.small_buckler.durability, "Should be equal"
        assert Small_Item.objects.get(pk=1).weight == self.small_buckler.weight, "Should be equal"
        assert Small_Item.objects.get(pk=1).description == self.small_buckler.description, "Should be equal"

    def test_create_large_item(self):
        assert Large_Item.objects.count() == 1, 'Should be equal'
        assert Large_Item.objects.get(pk=1) == self.large_shield, "Should be equal"
        assert Large_Item.objects.get(pk=1).item_name == self.large_shield.item_name, "Should be equal"
        assert Large_Item.objects.get(pk=1).effect == self.large_shield.effect, "Should be equal"
        assert Large_Item.objects.get(pk=1).durability == self.large_shield.durability, "Should be equal"
        assert Large_Item.objects.get(pk=1).weight == self.large_shield.weight, "Should be equal"
        assert Large_Item.objects.get(pk=1).description == self.large_shield.description, "Should be equal"
