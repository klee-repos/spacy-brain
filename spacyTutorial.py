
from flask import Blueprint, request
import spacy
from auth import Auth

spacy_tutorial = Blueprint('spacy_tutorial', __name__)


@spacy_tutorial.route("/parts-of-speech", methods=["POST"])
def statistical():
    try:
        auth = Auth(request.headers["Authorization"])
        status = auth.verifyToken()
        if status == "authorized":
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(request.json["input"])
            for token in doc:
                print(token.text, token.pos_)
            return "success"
        else:
            return "unauthorized", 501
    except:
        return "error", 500
