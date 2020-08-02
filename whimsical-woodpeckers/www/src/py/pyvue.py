
__pragma__ ('js', "console.log('test');")
__pragma__ ('js', "{}", "import * as VuePkg from 'vue';")
__pragma__ ('noalias', 'default')

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

    def __init__(self, el):
        self.el = el
        self.data = clone_data(self.data)
        methods = {func: getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")}
        self._vue = __new__(JSVue({
            "el": self.el,
            "data": self.data,
            "methods": methods
        }))


