from node.core.parser.node_parser_interface import NodeParserInterface


class ParserC(NodeParserInterface):
    def parse(self, message: str) -> str:
        """
        Parses the message using the awesome C algorithm.
        :param message: Message to parse.
        :return: Parsed message.
        """
        return f'C: {message}'
