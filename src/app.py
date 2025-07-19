from . import create_app
from flask import render_template
from .api import dices

app = create_app()

def render(file, **context):
    return render_template(file, _author="Marco Lenschau", **context)

@app.route('/')
@app.route('/<string:name>')
def home(name = None):
    return render("index.html", context=name)

@app.route('/dices/')
def handle_dices():
    return render('dices.html', _dices=dices)       