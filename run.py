# -*- coding: utf-8 -*-

"""
"""

from eve import Eve
import os
import twilio.twiml

app = Eve()


@app.route('/custom/your_late_call', methods=['GET', 'POST'])
def your_late_call():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey, your late bitch! Your going to be fined.")
    return str(resp)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.environ.get('PORT')) if 'PORT' in os.environ else 5000
    app.run(host=host, port=port, debug=True)