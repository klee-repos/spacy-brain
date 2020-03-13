import os
from dotenv import load_dotenv
load_dotenv()


class Auth:
    def __init__(self, token):
        self.token = token

    def verifyToken(self):
        if self.token == os.getenv("TOKEN"):
            return "authorized"
        else:
            return "unauthorized"
