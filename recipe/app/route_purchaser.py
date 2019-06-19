from flask import Blueprint, request
from app.service.purchaser_service import *
import json

purchaser = Blueprint('purchaser', __name__)


@purchaser.route('/purchaser', methods=['GET', 'POST'])
def purchaser_date():
    if request.method == 'GET':
        if request.is_json and request.get_json():
            i = request.get_json()
            result = get_my_purchaser(i)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            j = request.get_json()
            result = set_my_purchaser(j)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
