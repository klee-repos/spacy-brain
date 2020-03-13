import os
from auth import Auth
from flask import Flask, request
from spacyTutorial import spacy_tutorial
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.register_blueprint(spacy_tutorial, url_prefix="/spacy-tutorial")


@app.route("/", methods=["POST"])
def hello():
    return "Hello World!"


@app.route("/check-auth", methods=["POST"])
def checkAuth():
    auth = Auth(request.headers["Authorization"])
    authStatus = auth.verifyToken()
    return authStatus


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"), port=8080)
