import ConfigParser
import redis
from pyechonest import artist 
from pyechonest import config
from pyechonest import song
from pyes import *

redis_client = redis.Redis(host='localhost', port=6379, db=0)
es_conn = ES('127.0.0.1:9200')

# Reading Configs
cfg = ConfigParser.ConfigParser()
cfg.read('.config')
api_key = cfg.get('APIKeys', 'api_key')
config.ECHO_NEST_API_KEY=api_key


