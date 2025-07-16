from . import create_app
from flask import render_template, jsonify, request

app = create_app()
dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 20},
]

def render(file, **context):
    return render_template(file, _author="Marco Lenschau", **context)

@app.route('/')
@app.route('/<string:name>')
def home(name = None):
    return render("index.html", context=name)

@app.route('/dices/')
def handle_dices():
    return render('dices.html', _dices=dices)

@app.route('/api/dices', methods=["GET", "POST"])
def handle_dices_request():
    if request.method == "GET":
        return jsonify(dices=dices)
    else:
        try:
            payload = request.get_json()
            if not payload["numberOfSides"]:
                raise Exception
            if not payload["numberOfSides"] > 1:
                raise Exception
            new_dices = {"numberOfSides": payload["numberOfSides"]}
            if not payload["numberOfSides"] < 128:
                raise Exception
            new_dices = {"numberOfSides": payload["numberOfSides"]}
            if new_dices in dices:
                raise Exception
            dices.append(new_dices)

            return {"message": "dices created"}, 201
        except:   
            return {"message": "An Unknown Error accured"}, 500