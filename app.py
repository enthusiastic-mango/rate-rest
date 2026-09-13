from web_manager import WebManager

class App():
    def __init__(self):
        self._web_manager = WebManager()

    def run(self)->None:
        """ Запускает приложение """
        self._web_manager.run()