from Main import result
from flask import Flask
app = Flask(__name__)


@app.route("/")
def go():
    return result(), 200


if __name__ == '__main__':
    app.run(port=5000)
