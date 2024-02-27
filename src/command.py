"""Class for defining the content of the individual commands.
"""


class Command:
    def __init__(
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
        return (
            f'{self.name} {self.start_message} {self.end_message} '
            f'{self.suggestion_message} {self.gitr_help}'
        )
