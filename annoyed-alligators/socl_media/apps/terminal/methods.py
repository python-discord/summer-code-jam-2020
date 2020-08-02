class TerminalCommand():
    def __init__(self, option):
        self.specified_method = option.split()[0]
        self.params = option[option.find(" ") + 1:]

    def run(self):
        method_to_call = getattr(self, self.specified_method)
        response = method_to_call(self.params)
        return response

    @staticmethod
    def message(params=None):
        if params.count(' ') == 0:
            message = "Message text not provided <br>"\
                "Usage: message username message text"
        else:
            user = params.split()[0]
            print(user)
            message_text = params[params.find(" ")+1:]
            print(message_text)
            message = f"Message delivered to {user}."
        return message
