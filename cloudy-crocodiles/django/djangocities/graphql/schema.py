import os

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
)

from django.conf import settings

from .types import types

type_defs = load_schema_from_path(
    os.path.join(settings.BASE_DIR, "djangocities", "graphql", "schemas")
)

schema = make_executable_schema(type_defs, types)
