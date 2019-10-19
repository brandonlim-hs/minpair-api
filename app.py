from flask import Flask
import minpair
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "minpair API: " + minpair.__version__
