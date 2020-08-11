import factory
from django.contrib.auth.models import User
from core.models import Trader, InventoryRecord, QuantityType as QT
from core.factories.product import ProductFactory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"teabay_user_{n+1}")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(
        lambda obj: f"{obj.first_name}.{obj.last_name}@{factory.Faker('domain_name')}".lower()
    )

    class Meta:
        model = User


class TraderFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    description = factory.Faker("catch_phrase")

    class Meta:
        model = Trader


class InventoryRecordFactory(factory.DjangoModelFactory):
    owner = factory.SubFactory(TraderFactory)
    quantity = factory.Faker("pyint")
    quantity_type = factory.Iterator(
        [QT.COUNT.value, QT.WEIGHT_G.value, QT.WEIGHT_KG.value]
    )
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = InventoryRecord
