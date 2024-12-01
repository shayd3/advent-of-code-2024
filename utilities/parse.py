class Parse():

    @staticmethod
    def str_to_list(input: str, delimiter: str = '\n') -> list:
        """Parse the input on a given delimiter.

        Args:
            input (str): The input string.
            delimiter (str): The delimiter to split the input on. Defaults to '\n'.

        Returns:
            list: The input string split on the delimiter."""
        return [line for line in input.split(delimiter)]
