# -*- coding: utf-8 -*-

"""

"""

import os

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = int(os.environ.get('MONGO_PORT'))
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')

JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ISSUER = os.environ.get('JWT_ISSUER')
JWT_AUDIENCES = os.environ.get('JWT_AUDIENCES').split(', ')
JWT_ROLES_CLAIM = os.environ.get('JWT_ROLES_CLAIM').split(', ')
JWT_SCOPE_CLAIM = os.environ.get('JWT_SCOPE_CLAIM')



DOMAIN = {}
