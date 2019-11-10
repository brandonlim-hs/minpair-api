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
        generator = minpair.generator(**{
            # Use corpus data from layer instead of downloading at runtime
            'download_corpus': False,
            'pos': pos
        })
        return {
            "minimal_pairs": generator.vowel_minpair(vowels)
        }
    except Exception as e:
        return {
            "errors": [
                {"message": str(e)}
            ]
        }
