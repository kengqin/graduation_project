from flask import Blueprint, request
from app.service.mydetails_service import *
import json

my_details = Blueprint('my_details', __name__)


@my_details.route('/my_details', methods=['POST', 'GET'])
def my_detail():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            print(i)
            result = get_order_mydetails(i)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
@my_details.route('/my_insert', methods=['POST', 'GET'])
def my_insert():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            print(i)
            res = insert_order_mydetails(i)
            # print(res)
            if res:
                return json.dumps({'status_code':"10100","status_text":"评论成功"})
            else:
                return json.dumps({'status_code':"40100","status_text":"评论失败"})
        else:
            return json.dumps({"1102": "错误"})
