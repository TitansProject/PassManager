import configparser
import os.path


class FirebaseConfig:
    def __init__(self, config_file="conf.ini"):
        if os.path.isfile(config_file):
            print("Loading config from file: " + config_file)
            self.load_config_file(config_file)
        else:
            print("You have to create new config file called " + config_file)
            exit(0)

    def load_config_file(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.databaseURL = config.get("firebase_conf", "databaseURL")
