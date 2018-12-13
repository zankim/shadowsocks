# Config
NODE_ID = 17


# hour,set 0 to disable
SPEEDTEST = 6
CLOUDSAFE = 1
ANTISSATTACK = 0
AUTOEXEC = 0

MU_SUFFIX = 'zhaoj.in'
MU_REGEX = '%5m%id.%suffix'

SERVER_PUB_ADDR = '127.0.0.1'  # mujson_mgr need this to generate ssr link
API_INTERFACE = 'glzjinmod'  # glzjinmod, modwebapi

WEBAPI_URL = 'https://www2.avalyuan.com'
WEBAPI_TOKEN = 'glzjin'

# mudb
MUDB_FILE = 'mudb.json'

# Mysql
MYSQL_HOST = '89.208.254.57'
MYSQL_PORT = 3306
MYSQL_USER = 'sspanel'
MYSQL_PASS = 'Qaz150109'
MYSQL_DB = 'sspanel'

MYSQL_SSL_ENABLE = 1
MYSQL_SSL_CA = '/root/mysqlssl/sspanel/ca.pem'
MYSQL_SSL_CERT = '/root/mysqlssl/sspanel/client-cert.pem'
MYSQL_SSL_KEY = '/root/mysqlssl/sspanel/client-key.pem'

# API
API_HOST = '127.0.0.1'
API_PORT = 80
API_PATH = '/mu/v2/'
API_TOKEN = 'abcdef'
API_UPDATE_TIME = 60

# Manager (ignore this)
MANAGE_PASS = 'ss233333333'
# if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
# make sure this port is idle
MANAGE_PORT = 23333
