import factory
import random
from core.models.review import Review
from core.factories.trader import UserFactory
from core.factories.market import TradeFactory


class ReviewFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    trade = factory.SubFactory(TradeFactory)
    rating = factory.LazyFunction(lambda: random.randint(1, 5))
    description = factory.Faker("sentence")

    class Meta:
        model = Review
