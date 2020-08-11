import json
import pydoc
from typing import Iterable
from submission import Submission
from solution import Solution
from errors import ImplementationError


class Judge:
    """
    Class for determining if a solution is correct.
    It first reads function inputs from a json file, then
    runs those inputs in both the Solution and Submission
    class and checks for differences in output.
    """

    def __init__(self, infile: str):
        input_data = json.load(open(infile, "r"))

        self.func_name = input_data["name"]
        self.inputs = []

        raw_inputs = input_data["testcases"]

        for case in raw_inputs:
            variables = []

            for var in case:
                # Cast variable to the type specified in inputs.json
                type = pydoc.locate(var["type"])
                variable_val = type(var["value"])
                variables.append(variable_val)

            self.inputs.append(variables)

    def evaluate(self) -> bool:
        """

        The function will error out if either the submission
        function raises an error or the solution and submission
        outputs do not match

        Thank God for stackoverflow
        """

        solution = Solution()
        submission = Submission()

        # retrive the running functions in the Solution and Submission classes
        # The names of these functions are defined in inputs.json
        solution_func = getattr(solution, self.func_name)
        submission_func = getattr(submission, self.func_name)

        for testcase in self.inputs:
            # unpack each testcase and execute
            solution_res = solution_func(*testcase)
            submission_res = submission_func(*testcase)

            if isinstance(solution_res, Iterable):
                if sorted(solution_res) != sorted(submission_res):
                    raise ImplementationError(
                        f"Error for testcase {testcase}. "
                        f"Expected {solution_res}, "
                        f"got {submission_res}"
                    )
            else:
                if solution_res != submission_res:
                    raise ImplementationError(
                        f"Error for testcase {testcase}. "
                        f"Expected {solution_res}, "
                        f"got {submission_res}"
                    )


bob = Judge("inputs.json")
bob.evaluate()
