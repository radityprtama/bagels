# file is used with textual run --dev


from bunji.locations import set_custom_root

if __name__ == "__main__":
    set_custom_root("./instance/")

    from bunji.config import load_config

    load_config()

    from bunji.models.database.app import init_db

    init_db()

    from bunji.app import App

    app = App()
    app.run()
