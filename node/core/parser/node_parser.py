from random import Random

from node.core.parser.parser_a import ParserA
from node.core.parser.parser_b import ParserB
from node.core.parser.parser_c import ParserC


class NodeParser:

    def __init__(self) -> None:
        """
        Initializes a new NodeParser.
        """
        self.parser = self._pick_random_parser()

    def parse(self, message: str):
        """
        Parses the message using one of the parsers.
        :param message: Message to parse.
        :return: Parsed message.
        """
        return self.parser.parse(message)

    @staticmethod
    def _pick_random_parser():
        choise = Random().randint(0, 10)
        if choise < 3:
            return ParserA()
        elif choise < 7:
            return ParserB()
        elif choise <= 10:
            return ParserC()
