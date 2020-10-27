from flask import Flask, render_template, request, url_for
import sys
import emoji

application = Flask(__name__)
PORT = 3000

@application.route("/")
def index():
    isEmoji = request.args.get("emoji")
    if isEmoji == None:
        return render_template("index.html",
                               isEmoji=isEmoji)
    else:
        isEmoji = isEmoji.replace(" ", "")
        return render_template("index.html",
                               emoji=emoji.emojize(f":{isEmoji}:",use_aliases=True),
                               isEmoji=isEmoji)

if __name__ == "__main__":
    application.run(debug=True,port=PORT)
    sys.stdout.write(f"Server is listening on port {PORT}\n")