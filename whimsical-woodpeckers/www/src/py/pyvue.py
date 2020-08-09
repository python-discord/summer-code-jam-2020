# __pragma__ ('js', "{}", "import * as VuePkg from 'vue';")
# __pragma__ ('noalias', 'default')
# __pragma__ ('noalias', 'name')

# __pragma__ ('skip')
VuePkg = __new__ = this = console = __pragma__ = 0    # Prevent complaints by optional static checker
# __pragma__ ('noskip')


JSVue = VuePkg.default

LIFECYCLE = set(['created'])

def clone_data(data):
    if isinstance(data, dict):
        new_data = dict(data)
        # __pragma__ ('iconv')
        for key in new_data:
            new_data[key] = clone_data(new_data[key])
        # __pragma__ ('noiconv')
    elif isinstance(data, list):
        new_data = list(data)
        for i, data in enumerate(new_data):
            new_data[i] = clone_data(data)
    else:
        new_data = data
    return new_data


class Vue:
    data = {}
    template = ""
    components = {}

    def __init__(self, el):
        self.el = el
        self.data = clone_data(self.data)
        data = self.get_component()
        data['el'] = el
        self._vue = __new__(JSVue(data))

    def get_component(self):
        methods = {func: getattr(self, func) for func in dir(self) if
                   callable(getattr(self, func)) and not func.startswith("__")}
        data = {
            "data": self.data,
            "template": self.template
        }
        # __pragma__("tconv")
        if methods:
            data['methods'] = methods
        if self.components:
            data['components'] = self.components
        # __pragma__("notconv")
        return data


def making_component(comp):
    def func(one, two, three):
        console.log(one, two, three)
        return __new__(comp(one, two))
    return func


class Component:
    data = {}
    template = ""
    props = []
    components = {}

    def __init__(self):
        self._vue = self.get_component()
        JSVue.component(self.__class__.__name__.lower(), self._vue)

    @classmethod
    def get_component(cls):
        data = {
            "data": cls.get_data,
            "template": cls.template
        }

        # another = dir(cls)
        test = [func for func in dir(cls) if not func.startswith("__") and callable(getattr(cls, func))]
        # __pragma__("js", "{}", "let methods = {}")
        for i in test:
            func = getattr(cls, i)
            if i in LIFECYCLE:
                data[i] = func
            else:
                __pragma__("js", "{}", "methods[i] = func")

        # console.log(methods)

        # __pragma__("tconv")
        if methods:
            data['methods'] = methods
        if cls.components:
            data['components'] = cls.components
        if cls.props:
            data['props'] = cls.props
        # __pragma__("notconv")
        # console.log(data)
        return JSVue.extend(data)

    @classmethod
    def get_data(cls):
        return clone_data(cls.data)
