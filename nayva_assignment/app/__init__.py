#!flask/bin/python
from flask import Flask


app = Flask(__name__)

from app.urls import mod
app.register_blueprint(mod)


