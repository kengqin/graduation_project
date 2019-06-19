from flask import Blueprint, request
from app.service.travellers_service import *
import json

travellers = Blueprint('travellers', __name__)


@travellers.route('/travellers', methods=['GET', 'POST'])
def purchaser_date():
    if request.method == 'GET':
        if request.is_json and request.get_json():
            i = request.get_json()
            result = get_travellers_date(i)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            j = request.get_json()
            result = set_travellers_date(j)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
