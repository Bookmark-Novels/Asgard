import sys

sys.dont_write_bytecode = True

from app import app
from modules.secrets import secrets

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=secrets.port, threaded=secrets.DEBUG, debug=secrets.DEBUG)