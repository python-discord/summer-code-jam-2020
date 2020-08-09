from pyvue import Component


class User(Component):
    template = "#directory-user-template"
    props = ["name", "last_online", "id"]

#    def list_name(self):
#        return({ self.data.name })
