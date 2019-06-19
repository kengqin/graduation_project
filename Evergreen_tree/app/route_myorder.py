from flask import Blueprint, request
from app.service.myOrder_service import *
import json

myorder = Blueprint('myorder', __name__)


@myorder.route('/myorder', methods=['GET', 'POST'])
def my_order():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            result = get_order_detail_1(i)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
@myorder.route('/myorder_del', methods=['GET', 'POST'])
def my_order_del():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            print(i)
            result = del_order_detail_1(i)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})