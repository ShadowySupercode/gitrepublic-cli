import typer
import command


def test_command():

    """
    Main method for the gitr CLI.

    Each command is called as defined in the Command class.
    True interaction with the SDK will be defined at a later date.
    """

    cmd = command.Command(
        # Instantiate the gitr push command.
        "gitr push: ",
        "\nThis is the start message for the push function.",
        "\nThis is the end message for the push function.",
        "\nThis is the suggestion message for the push function.",
        "\nThis is the help message for the push function."
        )
    print(cmd)


if __name__ == '__main__':
    # protect the code from accidentally being run.
    typer.run(test_command)

# Instantiate the typer application
app = typer.Typer()
