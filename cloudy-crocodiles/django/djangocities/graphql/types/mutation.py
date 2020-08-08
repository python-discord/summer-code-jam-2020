from ariadne import MutationType
from djangocities.folders import mutation as folder_mutations
from djangocities.user import mutation as user_mutations

mutation = MutationType()

# User Mutations
mutation.set_field("login", user_mutations.resolve_login)
mutation.set_field("register", user_mutations.resolve_register)

# Folder Mutations
mutation.set_field("createFolder", folder_mutations.resolve_create_folder)
