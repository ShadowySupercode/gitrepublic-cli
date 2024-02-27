import typer
import command

"""Command line interface for GitRepublic. All commands are called from here.
"""


def test_command():
    cmd = command.Command(
             "gitr push: ",
             "\nThis is the start message for the push function.",
             "\nThis is the end message for the push function.",
             "\nThis is the suggestion message for the push function.",
             "\nThis is the help message for the push function."
             )
    print(cmd)


if __name__ == '__main__':
    typer.run(test_command)


app = typer.Typer()
