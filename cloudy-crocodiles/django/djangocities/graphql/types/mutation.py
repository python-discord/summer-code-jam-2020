from ariadne import MutationType
from djangocities.pages import mutation as page_mutations
from djangocities.user import mutation as user_mutations

mutation = MutationType()

# User Mutations
mutation.set_field("login", user_mutations.resolve_login)
mutation.set_field("register", user_mutations.resolve_register)

# Page Mutations
mutation.set_field("createPage", page_mutations.resolve_create_page)
mutation.set_field("updatePage", page_mutations.resolve_update_page)
