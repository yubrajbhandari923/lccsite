from .base import *

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "lumbinichessclub.herokuapp.com"]
try:
    from .local import *
except ImportError:
    pass
