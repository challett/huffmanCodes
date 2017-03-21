import logging
import os
import sys

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from calculate import insert_p, createCodes

log = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def error_404(notfound_exception):
    return index()

@socketio.on('calculateCodes')
def test_message(message):
    (codeDict, averageCodeLength, entropy) = createCodes(message["data"])
    emit('codeResponse', {'codes': codeDict, 'entropy': entropy, 'averageCodeLength': averageCodeLength})


if __name__ == '__main__':
    socketio.run(app, host=os.getenv('HOST', 'localhost'),
            port=int(os.getenv('PORT', '8080')),
            debug=bool(os.getenv('DEBUG_ON', '1')))
