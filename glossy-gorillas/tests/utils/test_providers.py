import pytest
from utils import providers
from typing import Generator
from hypothesis_auto import auto_pytest_magic as auto_test
import warnings
from hypothesis.errors import NonInteractiveExampleWarning

# ignore hypothesis warnings caused by `.example()` method call
warnings.filterwarnings("ignore", category=NonInteractiveExampleWarning)


@pytest.mark.parametrize(
    "generator,",
    [providers.SpiceGenerator, providers.ServiceGenerator, providers.ObjectGenerator],
)
def test_provider_generates_random_2_part_string(generator: Generator[str, None, None]):
    stringset = [next(generator) for _ in range(0, 50)]
    assert all([isinstance(x, str) for x in stringset])
    assert len(stringset) == len(list(set(stringset)))


auto_test(providers.random_permutations)
auto_test(providers._spice)
auto_test(providers._service)
auto_test(providers._object)
auto_test(providers._news_title)
