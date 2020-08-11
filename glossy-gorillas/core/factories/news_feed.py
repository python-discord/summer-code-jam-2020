import factory
from datetime import date
from faker import Faker
from core.models import NewsFeed
from utils.providers import NewsTitleGenerator


fake = Faker()


class NewsFeedFactory(factory.DjangoModelFactory):
    title = factory.LazyFunction(lambda: next(NewsTitleGenerator))
    location = factory.Faker("city")
    date_published = factory.LazyFunction(
        lambda: fake.date_between_dates(
            date_start=date(1600, 1, 1), date_end=date(1750, 1, 1)
        )
    )
    description = factory.Faker("paragraph")

    class Meta:
        model = NewsFeed
