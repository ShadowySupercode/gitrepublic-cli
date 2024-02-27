import command


class TestCommand:
    """Test of the basic Command class that covers all of the gitr calls."""

    def test_str(self):
        """Simple test to check if the test environment is correctly
        implemented and the Command class can be interacted with."""
        cmd = command.Command(
            "Test name",
            "Test start message",
            "Test end message",
            "Test suggestion message",
            "Test help message"
            )

        assert (isinstance(str(cmd), str))

    def test_init_not_str(self):
        """Simple test to check if the command class correctly types."""
        cmd = command.Command(
            "gitr made-up name",
            13,
            "This is the end message that we test.",
            "The suggestion message that we test.",
            "This is the help message that we test."
            )

        check_for_integer = not isinstance(cmd, str)
        assert (check_for_integer is True)

    def test_init_same_content(self):
        """Simple test to check if the command class returns what I sent it."""
        cmd = command.Command(
            "gitr made-up name",
            13,
            "This is the end message that we test.",
            "The suggestion message that we test.",
            "This is the help message that we test."
            )

        test_name = "gitr made-up name"
        test_start_message = 13
        test_end_message = "This is the end message that we test."
        test_suggestion_message = "The suggestion message that we test."
        test_gitr_help = "This is the help message that we test."

        assert (cmd.name == test_name)
        assert (cmd.start_message == test_start_message)
        assert (cmd.end_message == test_end_message)
        assert (cmd.suggestion_message == test_suggestion_message)
        assert (cmd.gitr_help == test_gitr_help)
