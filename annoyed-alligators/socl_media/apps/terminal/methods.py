class TerminalCommand():
    """Container for terminal all terminal commands"""

    def __init__(self, option):
        self.specified_method = option.split()[0]
        self.params = option[option.find(" ") + 1:]

    def run(self):
        method_to_call = getattr(self, self.specified_method)
        response = method_to_call(self.params)
        return response

    @staticmethod
    def message(params=None):
        help_text = "message: use this to send messages<br><br>"\
            "Usage: message username [args] [message text]<br>"\
            "options:<br>"\
            "--help: get help (this screen)<br>"\
            "--e: encrypt the message<br>"\
            "--last: view the last message sent to the user<br>"

        if params.split()[0] == '--help':
            message = help_text
        elif params.count(' ') == 0:
            message = "Message text not provided <br>"\
                "Usage: message username message text"
        else:
            user = params.split()[0]
            message = f"Message delivered to {user}."
        return message
