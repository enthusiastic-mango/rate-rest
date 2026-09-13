from web_manager import WebManager
from database_manager import DatabaseManager
from typing import Dict
import json

class App():
    def __init__(self, config_filepath: str):
        self._config: Dict = self._read_config(config_filepath)
        
        self._web_manager: WebManager = self._create_web_manager()
        self.database_manager: DatabaseManager = self._create_database_manager()

    def run(self) -> None:
        """ Запускает приложение """
        self._web_manager.run()

    def _read_config(self, filepath: str) -> Dict:
        " Читает JSON с конфигом "
        with open(filepath) as file:
            config = json.load(file)
            return config

    def _create_web_manager(self) -> WebManager:
        return WebManager()

    def _create_database_manager(self) -> DatabaseManager:
        database_filepath = self._config.get("database_filepath")
        return DatabaseManager(database_filepath)