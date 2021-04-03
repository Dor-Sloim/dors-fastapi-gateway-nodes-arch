import uuid
import os

from node.core.parser.node_parser import NodeParser
from loguru import logger


class NodeState:
    def __init__(self, ) -> None:
        """
        Initializes a new NodeState.
        """
        self.messages = dict()
        self.parser = NodeParser()
        self.service_id = str(uuid.uuid4())
        self.hostname = os.environ["HOSTNAME"]
        self.port = os.environ["PORT"]
        logger.debug(f'self.hostname:{self.hostname}')
        logger.debug(f'self.port:{self.port}')

    def add_message(self, message: str) -> str:
        """
        Adds new message to the state
        :param message: The message to add to state.
        :return: the id of the message.
        """
        mess_id = str(uuid.uuid4())
        parsed_message = self.parser.parse(message)
        self.messages[mess_id] = {
            "id": mess_id,
            "message": message,
            "parsed": parsed_message,
            'serviceId': self.service_id
        }
        return mess_id

    def get_message_by_id(self, mess_id: str) -> dict:
        """
        Returns the message from state by its id.
        :param mess_id: The message id.
        :return: Dictionary of the message object.
        """
        return self.messages[mess_id]
