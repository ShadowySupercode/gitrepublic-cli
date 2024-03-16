class Command:

    """Class for defining the individual commands that the CLI will call."""

    def __init__(
        # Constructor for the Command class.
        self: str,
        name: str,
        start_message: str,
        end_message: str,
        suggestion_message: str,
        gitr_help: str
            ):
        self.name = name
        self.start_message = start_message
        self.end_message = end_message
        self.suggestion_message = suggestion_message
        self.gitr_help = gitr_help

    def __str__(self):
        # Function to return a string version of Command object.
        return (
            f'{self.name} {self.start_message} {self.end_message} '
            f'{self.suggestion_message} {self.gitr_help}'
        )
