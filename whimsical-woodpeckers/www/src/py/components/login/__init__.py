from pyvue import Component


class Login(Component):
    template = "#login-template"

    props = ['mode']

    @staticmethod
    def login(self):
        pass
