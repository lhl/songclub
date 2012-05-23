"""
This expects an .config file with the following sections:
[API Keys]
api_key=1234567890

[TOOLS]
enmfp_codegen=/path/to/enmfp/codegen
"""
import configparser
config = configparser.ConfigParser()
config.read('.api_keys')
api_key = config['API Keys']['api_key']

from pyechonest import config 
config.ECHO_NEST_API_KEY=api_key

import subprocess
import json

# Get the JSON ENMFP from an MP3
def get_enmfp_from_mp3(mp3_path):
  json_str = subprocess.check_output([config['Tools']['enmfp_codegen'], mp3_path, 10, 10]).decode('utf-8')
  result = json.loads(json_str)
  return result

