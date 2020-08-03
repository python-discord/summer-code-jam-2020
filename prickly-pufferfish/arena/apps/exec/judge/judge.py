import json
import pydoc
from .submission import Submission
from .solution import Solution
from .errors import ImplementationError


class Judge:
    """
    Class for determining if a solution is correct.
    It first reads function inputs from a json file, then
    runs those inputs in both the Solution and Submission
    class and checks for differences in output.
    """

    def __init__(self, infile: str):
        input_data = json.load(open(infile, 'r'))

        self.func_name = input_data['name']
        self.inputs = []

        raw_inputs = input_data['testcases']

        for case in raw_inputs:
            variables = []

            for var in case:
                type = pydoc.locate(var['type'])
                variable_val = type(var['value'])
                variables.append(variable_val)

            self.inputs.append(variables)

    def test(self):
        pass

