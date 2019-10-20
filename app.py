from flask import Flask, request
import minpair
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "minpair API: " + minpair.__version__


@app.route("/vowel", methods=["GET"])
def vowel_minpair():
    vowels = request.args.getlist("vowels")
    pos = request.args.getlist("pos")
    try:
        minpairs = minpair.vowel_minpair(vowels, pos)
        return {
            "minimal_pairs": minpair.vowel_minpair(vowels, pos)
        }
    except Exception as e:
        return {
            "errors": [
                {"message": str(e)}
            ]
        }
