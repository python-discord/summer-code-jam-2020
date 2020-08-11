
class ImplementationError(BaseException):
    """
    A custom error class meaning that a solution has errored
    """

    def __init__(self, *args):
        if args:
            self.error_msg = args[0]
        else:
            self.error_msg = ""

    def __str__(self):
        if self.error_msg:
            return self.error_msg
        else:
            return "ImplementationError raised"
