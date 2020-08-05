__pragma__ ('js', "{}", "import * as VuePkg from 'vue';")
__pragma__ ('noalias', 'default')
__pragma__ ('noalias', 'name')

JSVue = VuePkg.default


def clone_data(data):
    if isinstance(data, dict):
        new_data = dict(data)
        __pragma__ ('iconv')
        for key in new_data:
            new_data[key] = clone_data(new_data[key])
        __pragma__ ('noiconv')
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

    def __init__(self, el):
        self.el = el
        self.data = clone_data(self.data)
        methods = {func: getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")}
        self._vue = __new__(JSVue({
            "el": self.el,
            "data": self.data,
            "methods": methods
        }))


def making_component(comp):
    def func(one, two, three):
        console.log(one, two, three)
        return __new__(comp(one, two))
    return func


class Component:
    data = {}
    template = ""
    props = []

    def __init__(self):
        self.data = clone_data(self.data)
        self._data = 0
        methods = {func: getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")}
        console.log(self.template)
        self._vue = JSVue.extend({
            "data": self.get_data,
            "methods": methods,
            "template": self.template,
            "props": self.props
        })
        console.log(self.__class__.__name__, self._vue)
        JSVue.component(self.__class__.__name__.lower(), self._vue)

    def get_data(self):
        self._data += 1
        console.log(self._data)
        return clone_data(self.data)

#
#
# def createComponent(one, two):
#     console.log(this, one, two)
#
# class Component:
#     data = {}
#     props = []
#     template = ""
#     _registration = None
#     name = ""
#     methods = {}
#
#     def __init__(self):
#         self.name = self.name
#         self.data = clone_data(self.data)
#         self.methods = {func: getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")}
#         # self._vue = __new__(JSVue.component(self.name, self.__class__))
#
#     @classmethod
#     def get_data(cls):
#         return clone_data(cls.data)
#
#     @classmethod
#     def create_data(cls):
#         # methods = {func: getattr(cls, func) for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")}
#         data = clone_data(cls.data)
#         methods = dict(cls.methods)
#         methods['created'] = createComponent
#         console.log(methods)
#         return {
#             "name": cls.name,
#             "data": cls.get_data,
#             "methods": methods,
#             "template": cls.template
#         }
#
#
#
#
#     @classmethod
#     def register(cls, name):
#         name = name
#         if not name:
#             name = cls.__name__
#         cls.name = name
#         console.log(name, cls)
#         data = cls.create_data()
#         console.log(data)
#         cls._registration = JSVue.component(name, data)
#
#
#
