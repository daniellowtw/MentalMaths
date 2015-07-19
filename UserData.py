__author__ = 'Daniel'

import pickle
import configparser


class UserData:
    _filename = "score.db"
    db = {}

    def __init__(self, filename=None):
        if filename is not None:
            self._filename = filename

    def save_db(self):
        pickle.dump(self.db, open(self._filename, 'wb'))

    def load_or_create_db(self):
        """Tries to load the share and lookup dictionaries. Throws an
        exception if file does not exist.
        """
        try:
            with open(self._filename, 'rb') as f:
                self.db = pickle.load(f)
        except FileNotFoundError:
            pass

_config_file = 'setting.ini'
config = configparser.ConfigParser()

def gen_default_config_file():
    config.add_section('General')
    config.set('General', 'SHOW_TIMER', 'true')
    config.set('General', 'PAUSE_AFTER_QUESTION', 'false')
    config.add_section('Debug')
    config.set("Debug", 'Mode', 'false')
    with open(_config_file, 'w') as f:
        config.write(f)

def read_config_file():
    try:
        open(_config_file)
        config.read(_config_file)
    except FileNotFoundError as e:
        raise e

try:
    read_config_file()
except FileNotFoundError:
    gen_default_config_file()
