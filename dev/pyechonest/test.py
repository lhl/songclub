"""
This expects an .api_keys file with the following section:
[API Keys]
api_key=1234567890
"""
import configparser
config = configparser.ConfigParser()
config.read('.api_keys')
api_key = config['API Keys']['api_key']

from pyechonest import config 
config.ECHO_NEST_API_KEY=api_key


