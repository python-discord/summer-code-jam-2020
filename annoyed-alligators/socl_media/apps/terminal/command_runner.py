from .commands import Command


class TerminalCommandRunner():
    """This class interprets the command entered and triggers its run."""

    def __init__(self, command_string: str, request):
        self.specified_method = command_string.split()[0]
        if len(command_string.split()) > 1:
            self.params = command_string[command_string.find(" ") + 1:]
        else:
            self.params = ''
        self.request = request

    def run(self, **kwargs):
        found = False

        for command in Command.commands_list:
            if command.name == self.specified_method:
                found = True
                if '--help' in self.params:
                    # Return help text for the command
                    return {'response': command.help_text}
                else:
                    # Run the action function of the command
                    return command.action(self.request, self.params, **kwargs)

        if not found:
            # Invalid command
            return {'response': f"{self.specified_method}: Command not found. Please enter a valid command."}        
