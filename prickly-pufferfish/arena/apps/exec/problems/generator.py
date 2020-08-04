import json
import random
import string
from pprint import pprint


class typing:
    pass


class Generator:
    """
    a class for generating testcases
    """

    def __init__(self):
        pass

    def generate(self, func_name: str, types: list, num=10):
        json_obj = {
            'name': func_name,
            'testcases': []
        }

        for i in range(num):
            testcases = json_obj['testcases']
            current_case = []

            for var_type in types:
                print(var_type)
                var_case = {}

                if var_type == 'int':
                    var_case['type'] = 'int'
                    var_case['value'] = i

                elif var_type == 'str':
                    var_case['type'] = 'string'
                    var_case['value'] = self.gen_string()

                elif var_type == 'list[int]':
                    len = random.randint(1, 500)
                    int_list = [random.randint(1, 500) for x in range(len)]

                    var_case['type'] = 'list'
                    var_case['value'] = int_list

                current_case.append(var_case)

            testcases.append(current_case)

        with open('inputs.json', 'w', encoding='utf-8') as f:
            json.dump(json_obj, f, ensure_ascii=False, indent=4)

    def gen_int(self, min_val=0, max_val=65535):
        return random.randint(min_val, max_val)

    def gen_float(self, min_val=0, max_val=65535):
        return random.uniform(min_val, max_val)

    def gen_string(self, length=10):
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))


bob = Generator()
bob.generate('valid_pairs', ['int'])
