# -*- coding: utf-8 -*-

"""
"""

from eve import Eve
import os
from phone import blueprint


app = Eve()

app.register_blueprint(blueprint, url_prefix='/phone')
def pre_contacts_post(resource, request):
    print(resource)
    print(request.data)
app.on_pre_POST += pre_contacts_post
if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.environ.get('PORT')) if 'PORT' in os.environ else 5000
    app.run(host=host, port=port, debug=True)