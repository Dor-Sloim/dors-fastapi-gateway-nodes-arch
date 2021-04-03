class NodeParserInterface:
    """
    Interface representing a parser.
    """

    def parse(self, message: str) -> str:
        """
        Parses the given message.
        :param message: Received message to parse.
        :return: The parsed message.
        """
        pass
