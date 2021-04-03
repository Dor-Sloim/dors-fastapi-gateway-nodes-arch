from node.core.parser.node_parser_interface import NodeParserInterface


class ParserB(NodeParserInterface):
    def parse(self, message: str) -> str:
        """
        Parses the message using the awesome B algorithm.
        :param message: Message to parse.
        :return: Parsed message.
        """
        return f'B: {message}'
