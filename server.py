from flask import Flask
from flask_cors import CORS
from flask import request
from flask import Response

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)
CORS(app)

HOST="0.0.0.0"
PORT=6547
INFO = "To format code, POST JSON with the following format: {\"lang\": \"language\", \"code\": \"your code here\"}. Without the \"lang\" key, pygments will try to guess the language."

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        payload = request.form
        code = payload["code"]
        if "lang" in payload:
            lang = payload["lang"]
            lexer = get_lexer_by_name(lang)
        else:
            lexer = guess_lexer(code)
        html = highlight(code, lexer, HtmlFormatter())
        return Response(html, mimetype="text/plain")
    else:
        return Response(INFO, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
