from . import create_app
from flask import render_template

app = create_app()

def render(file, context = None, author = "Marco Lenschau"):
    return render_template(file, _name=context, _author=author)

@app.route('/')
@app.route('/<string:name>')
def home(name = None):
    return render("index.html", context=name)

@app.route('/dices/')
@app.route('/dices/<number>')
def handle_dices(number=None):
    return render('dices.html')