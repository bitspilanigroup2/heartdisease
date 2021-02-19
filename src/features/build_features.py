import configparser


def encodeColumns(self):
    """[summary]
    """
    config = configparser.ConfigParser()
    config.read('FILE.INI')
    print(config['DEFAULT']['path'])     # -> "/path/name/"
