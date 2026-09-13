from app import App

if __name__ == "__main__":
    config_file = "config.json"
    app = App(config_file)
    app.run()