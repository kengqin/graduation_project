from flask import Blueprint, request
from app.service.search_service import *
from flask import make_response
import json
search = Blueprint('search',__name__)

@search.route('/search_1', methods=['GET', 'POST'])
def search_1():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            search_1 = request.get_json()
            result = search1(search_1)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@search.route('/search_2', methods=['GET', 'POST'])
def search_2():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            search_2 = request.get_json()
            # print(search_2)
            result = search2(search_2)
            if result:
                response = make_response()
                response.data = json.dumps({"status_code": "11200", "text": result})

                # print(result)
                # print(response.data)
                return response
            else:
                return json.dumps({"status_code": "41404", "status_text": "没有查询到该景点"})

        else:
            return json.dumps({"status_code":"41404","status_text":"没有查询到该景点"})


@search.route('/search_3', methods=['GET', 'POST'])
def search_3():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            search_3 = request.get_json()
            # print(search_2)
            result = search3(search_3)
            response=make_response()
            response.data=json.dumps({"status":"200","text":result})

            # print(result)
            # print(response.data)
            return response
        else:
            return json.dumps({"1102":"错误"})