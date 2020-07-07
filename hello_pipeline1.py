#!/usr/bin/python
from flask import Flask

PORT = 9090
MESSAGE = ''' AAAAAAAAAAAAAAAAAAAAAAAAAA <br/><br/><br/><br/><br/><br/><br/><br/>
Welcome back Fahad AAAAAAAAAAAAAAAAAAAAAAAAAAAAA <br/><br/>
!!!!!!!!!!!!!!!!!Bismillah!!!!!!!!!!!!!!!!!  <br/><br/>
Knowledge necessitates actions, and actions in Islam are only accetped once they fulfil two condtions.<br/><br/>
these conditions are 1. Doing the action sincerely for Allah.<br/>
2. That the action is done in accordance to the Sunnah of the Prophet (May the peace and blessings of Allah be upon him).<br/>\n'''

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=PORT)
