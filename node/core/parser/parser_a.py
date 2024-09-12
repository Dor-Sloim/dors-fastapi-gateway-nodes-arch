from node.core.parser.node_parser_interface import NodeParserInterface


class ParserA(NodeParserInterface):
    def parse(self, message: str) -> str:
        """
        Parses the message using the awesome A algorithm.
        :param message: Message to parse.
        :return: Parsed message.
        """
        return f'A: {message}'
