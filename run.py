# -*- coding: utf-8 -*-

"""
"""

from eve import Eve
import os
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Eve()

SERVICE_URL = os.environ.get('SERVICE_URL')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_VOICE = os.environ.get('TWILIO_VOICE')

twilio_client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/custom/dial/your_late', methods=['GET'])
def your_late_dial():
    twilio_client.calls.create(to="+9720586021466", from_=TWILIO_VOICE, url=SERVICE_URL+'/custom/call/your_late')
    return 'dialing'


@app.route('/custom/call/your_late', methods=['GET', 'POST'])
def your_late_call():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey, your late bitch! Your going to be fined.")
    return str(resp)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.environ.get('PORT')) if 'PORT' in os.environ else 5000
    app.run(host=host, port=port, debug=True)