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

PUBLIC_METHODS = ITEM_METHODS = ['GET', 'POST', 'PATCH',
                                                  'PUT', 'DELETE']
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
BULK_ENABLED = True
X_DOMAIN = '*'

user = {
    'schema': {
        'first_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'last_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            # 'required': True,
            'unique': True,
        },
        'program': {'type': 'string'},
        'phone_number': {'type': 'string'},
        'gender': {'type': 'string'},
        'year': {'type': 'string'},
        'email': {'type': 'string'},

        # 'resource_methods': ['GET', 'POST'],
        # 'bulk_enabled': True
    }

}

checkin = {
    'schema': {
        'coor': {
            'type': 'point',
            'required': True
        },
        'time': {
            'type': 'datetime',
            'required': True
        },
        'user': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'users',
                'field': '_id',
                'embeddable': True
            }
        }
    }

}

DOMAIN = {'user': user, 'checkin':checkin}
