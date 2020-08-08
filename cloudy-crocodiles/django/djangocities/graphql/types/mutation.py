from ariadne import MutationType
from djangocities.user import mutation as user_mutations

mutation = MutationType()

# User Mutations
mutation.set_field("login", user_mutations.resolve_login)
mutation.set_field("register", user_mutations.resolve_register)

