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

#DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

PUBLIC_METHODS = ITEM_METHODS = ['GET', 'POST', 'PATCH',
                                                  'PUT', 'DELETE']
# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']


# Public enabled collections methods
PUBLIC_METHODS = ['GET']

# Public enabled item methods
PUBLIC_ITEM_METHODS = ['GET']

# We enable standard client cache directives for all resources exposed by the
# API, to 20 sec. We can always override these global settings later.
CACHE_CONTROL = 'max-age=00'
CACHE_EXPIRES = 20

# Max numper of records per page
PAGINATION_LIMIT = 2000

# Disable XML - cause it sucks
XML = False

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
# Enable Cross-Origin request from all domains - TMP
X_DOMAINS = '*'
X_ALLOW_CREDENTIALS = '*'

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
        # 'bulk_enabled': True d
    }

}

"""
{
    location: {
        "type": "Point",
        "coordinates": [10,20]
    },
    time: '2012-05-29T19:30:03.283Z',
    user: '56aa76b0cfc207b71181fce4'
}
"""
checkin = {
    'schema': {
        # 'b':{'type':'string'}
        'geo': {
            'type': 'point',
            'required': True
        },
        'time': {
             'type': 'datetime',
             'required': True
         },
        'user': {
            'type': 'objectid'
        }
    }

}

DOMAIN = {'user': user, 'checkin':checkin}
