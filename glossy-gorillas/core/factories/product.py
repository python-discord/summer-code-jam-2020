import factory
from core.models.product import Product, ProductType as PT
from utils import providers


class ProductFactory(factory.DjangoModelFactory):
    name = factory.Iterator(
        [
            next(providers.ServiceGenerator),
            next(providers.SpiceGenerator),
            next(providers.ObjectGenerator),
        ]
    )
    product_type = factory.Iterator([PT.SERVICE.value, PT.SPICE.value, PT.OBJECT.value])

    class Meta:
        model = Product
