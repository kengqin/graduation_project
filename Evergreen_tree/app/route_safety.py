from flask import Blueprint, request
from app.service.safety_service import *
import json

safety = Blueprint('safety', __name__)


@safety.route('/safety', methods=['GET', 'POST'])
def my_safety():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            result = chechk_info(i)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
