from typing import Hashable, Any, Dict, Union

import yaml


class ConfHandler:

    def __init__(self, conf_file_path: str) -> None:
        """
        Initializes a new configuration handler.
        :param conf_file_path: string representing the path to the configuration file.
        Should contain the yaml extension as well.
        """
        self.conf_file_path = conf_file_path
        self.conf = dict()

    def read_from_file(self) -> Union[Dict[Hashable, Any], list, None]:
        """
        Reads a yaml config file from self.conf_file_path.
        :return: Config dict
        """
        with open(self.conf_file_path) as conf_file:
            self.conf = yaml.load(conf_file, Loader=yaml.FullLoader)
            print(f'conf: {self.conf}')
            return self.conf
