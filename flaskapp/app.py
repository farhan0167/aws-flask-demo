from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
        "message": "Hello World",
        "host": socket.gethostname(),
        "ip-address": socket.gethostbyname(socket.gethostname())
    }

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
