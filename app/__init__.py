from flask import Flask, escape, request

app = Flask(__name__)

from .views import cliente_view
