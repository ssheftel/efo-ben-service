import os
from flask import Blueprint, current_app as app, request, Response
import twilio.twiml
from twilio.rest import TwilioRestClient
from time import sleep
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper



blueprint = Blueprint('phone', __name__)



SERVICE_URL = os.environ.get('SERVICE_URL')

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_VOICE = os.environ.get('TWILIO_VOICE')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

twilio_client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)




def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


def get_dconfig(cfg_name):
    cfg = app.data.driver.db['dconfig'].find_one({'cfg_name':cfg_name})
    return cfg


@blueprint.route('/txt', methods=['POST'])
@crossdomain(origin='*', attach_to_all=True, headers=['Content-Type'])
def txt():
    """
    {'to': '+123'}
    """
    data = request.get_json()
    twilio_client.messages.create(to=data['to'], from_=TWILIO_NUMBER, body="You're Late!")
    return Response(status=200)


@blueprint.route('/dial', methods=['POST'])
@crossdomain(origin='*', attach_to_all=True, headers=['Content-Type'])
def phone_dial():
    """
    payload {to: "", ?call_script_id: ""|call_script_text:""}must have attr to: '+972....'
    :return:
    """
    data = request.get_json()
    if not data.get('to', None): return Response(status=400)
    # call_script_id = data.get('call_script_id', "56aa4c8bb0bca60023000000")
    # if data.get('call_script_text', None):
    #     call_script_id = str(app.data.driver.db['callscripts'].insert_one({
    #         "script_text": data['call_script_text']
    #     }).inserted_id)
    #call_url = '{}/phone/call/{}'.format(SERVICE_URL, call_script_id)
    # call_url = '{}/phone/call'.format(SERVICE_URL, call_script_id)
    call_url = '{}/phone/call'.format(SERVICE_URL)
    twilio_client.calls.create(to=data['to'],
                               from_=TWILIO_VOICE,
                               url=call_url)
    return Response(status=200)


@blueprint.route('/call', methods=['GET', 'POST'])
@crossdomain(origin='*', attach_to_all=True, headers=['Content-Type'])
def call():
    # print(request.args.get('call_script_id'))
    # call_script = app.data.driver.db['callscript'].find_one({"_id": request.args.get('call_script_id')})
    # print(call_script)
    # script_text = call_script['script_text']
    script_text = "Your Late! Get your ass over to chi's to pay you're fine"
    resp = twilio.twiml.Response()
    resp.say(script_text)
    return str(resp)

