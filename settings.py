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

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

user = {
    'first_name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'last_name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
     'resource_methods': ['GET', 'POST']
}

DOMAIN = {'user': user}
