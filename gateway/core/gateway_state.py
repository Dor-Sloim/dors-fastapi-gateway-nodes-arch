class GatewayState:

    def __init__(self) -> None:
        """
        Initializes a new GatewayState.
        """
        self.nodes = list()

    def add_node(self, node_domain: str):
        """
        Attempts to add a new node to the state.
        :param node_domain:
        :return: True if added successfully, False otherwise.
        """
        if self._is_valid_node(node_domain):
            self.nodes.append(node_domain)
            return True
        return False

    def _is_valid_node(self, node_domain: str):
        """
        Check whether the the given node is valid.
        :param node_domain: node to validate
        :return: True if valid node, False otherwise.
        """
        return node_domain not in self.nodes
