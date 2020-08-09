# # __pragma__('alias', 'js_fetch', 'fetch')

# __pragma__ ('skip')
console = __new__ = js_fetch = URL = JSON = window = 0   # Prevent complaints by optional static checker
# __pragma__ ('noskip')


# __pragma__("kwargs")
# __pragma__('jsiter')


def dict_to_iterdict(thing):
    pls = {}
    for i in thing:
        pls[i] = thing[i]
    return pls


class Fetch:
    @staticmethod
    def get(url, params=None, headers=None, data=None):
        if data is None:
            data = {}
        else:
            data = dict_to_iterdict(data)  # necessary to get that jsiter sauce
        if headers is None:
            headers = {}
        else:
            headers = dict_to_iterdict(headers)  # necessary to get that jsiter sauce
        if params is None:
            params = {}
        full_data = {
            'method': 'GET',
            'headers': headers
        }
        console.log(url, type(url))
        full_data.update(data)
        url = window.location.href + url
        url = __new__(URL(url))
        # __pragma__('js', 'Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))')
        console.log(url, full_data)
        thing = window.fetch(url.href, full_data)
        return thing

    @staticmethod
    def post(url, params=None, headers=None, data=None):
        if data is None:
            data = {}
        else:
            data = dict_to_iterdict(data)  # necessary to get that jsiter sauce
        if headers is None:
            headers = {}
        else:
            headers = dict_to_iterdict(headers)  # necessary to get that jsiter sauce
        if params is None:
            params = {}
        full_data = {
            'method': 'POST',
            'headers': headers,
            'body': JSON.stringify(params)
        }
        full_data.update(data)
        thing = window.fetch(url, full_data)
        return thing


# __pragma__('nojsiter')
# __pragma__("nokwargs")


def fetch_demo():
    def callback(data):
        console.log("got back data!", data)

    # You can look online to see how lambdas work
    # but just copy this for now
    Fetch.get("https://httpbin.org/get", {'hello': 'there'}, headers={'pls': 'work'}) \
        .then(lambda response: response.json()) \
        .then(lambda data: callback(data))


def post_demo():
    def callback(data):
        console.log("got back data!", data)

    Fetch.post("https://httpbin.org/post", {'hello': 'there'}, headers={'pls': 'work'}) \
        .then(lambda response: response.json()) \
        .then(lambda data: callback(data))


# fetch_demo()
# post_demo()
