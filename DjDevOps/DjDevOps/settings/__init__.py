from .base import *
import os

env_mode = os.getenv('ENV_MODE')

if env_mode == 'prod':
   from .prod import *
elif env_mode == 'dev':
   from .dev import *
