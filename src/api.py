from flask import Blueprint, request, jsonify

api_bp = Blueprint("api", __name__)

dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 20},
]

@api_bp.route('dices', methods=["GET"])
def handle_get_request():
    return jsonify(dices=dices)

@api_bp.route('dices', methods=["POST"])
def handle_post_request():
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