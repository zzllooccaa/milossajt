from flask import Blueprint, views

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>TEST</h1> "
