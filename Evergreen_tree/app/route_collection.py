from flask import Blueprint, request
from app.service.mycollection_service import *
import json

my_collection = Blueprint('my_collections', __name__)


@my_collection.route('/my_collections', methods=['GET', 'POST'])
def my_collections():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = get_my_collection(i)
            # print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
@my_collection.route('/my_collections_del', methods=['GET', 'POST'])
def my_collections_del():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = del_my_collection(i)
            # print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
@my_collection.route('/select_college', methods=['GET', 'POST'])
def select_college():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = select_my_collection(i)
            print(result)
            return json.dumps({"status_code":"12000","status_text":"获取收藏数成功！","college":result})
        else:
            return json.dumps({"status_code":"42000","status_text": "获取收藏数错误"})
@my_collection.route('/select_counter', methods=[ 'POST'])
def select_counter():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = select_my_counter(i)
            print(result)
            return json.dumps({"status_code":"13000","status_text":"获取点赞数成功！","counter":result})
        else:
            return json.dumps({"status_code":"42000","status_text": "获取点赞数错误"})

@my_collection.route('/select_collegeon', methods=[ 'POST'])
def select_collegeon():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = select_college_on_1(i)
            if result:
                print(result)
                return json.dumps({"status_code":"18000","status_text":"存在收藏"})
            else:
                return json.dumps({"status_code":"18001","status_text":"不存在收藏"})
        else:
            return json.dumps({"status_code":"42000","status_text": "获取收藏信息错误"})
@my_collection.route('/insert_collegeon', methods=[ 'POST'])
def insert_collegeon2():

    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = insert_college_on_1(i)
            if result:
                return json.dumps({"status_code":"15000","status_text":"收藏成功"})
            else:
                return json.dumps({"status_code":"15001","status_text":"不存在收藏"})
        else:
            return json.dumps({"status_code":"42000","status_text": "获取收藏信息错误"})
@my_collection.route('/delete_collegeon', methods=[ 'POST'])
def delete_collegeon3():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = delete_college_on_1(i)

            return json.dumps({"status_code":"16000","status_text":"删除收藏成功"})

        else:
            return json.dumps({"status_code":"42000","status_text": "获取点赞信息错误"})
@my_collection.route('/select_counteron', methods=['POST'])
def select_counteron3():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = select_counter_on_2(i)
            if result:
                print(result)
                return json.dumps({"status_code":"14000","status_text":"存在点赞"})
            else:
                return json.dumps({"status_code":"14001","status_text":"不存在点赞"})
        else:
            return json.dumps({"status_code":"42000","status_text": "获取点赞信息错误"})
@my_collection.route('/insert_counteron', methods=[ 'POST'])
def insert_counteron2():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = insert_counter_on_1(i)
            if result:
                print(result)
                return json.dumps({"status_code":"15000","status_text":"点赞成功"})
            else:
                return json.dumps({"status_code":"15001","status_text":"不存在点赞"})
        else:
            return json.dumps({"status_code":"42000","status_text": "获取点赞信息错误"})
@my_collection.route('/delete_counteron', methods=['POST'])
def delete_counteron3():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = delete_counter_on_1(i)

            return json.dumps({"status_code":"16000","status_text":"删除点赞成功"})

        else:
            return json.dumps({"status_code":"42000","status_text": "获取点赞信息错误"})

@my_collection.route('/select_counts', methods=['POST'])
def select_counts():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = select_uer_count(i)
            if result:
                return json.dumps({"status_code": "16000", "status_text": "获取总点赞成功", "result": result})
            else:
                return json.dumps({"status_code":"42000","status_text": "获取总点赞信息错误"})
        else:
            return json.dumps({"status_code": "42000", "status_text": "获取总点赞信息错误"})
@my_collection.route('/select_colleges', methods=['POST'])
def select_colleges():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = select_uer_college(i)
            if result:
                return json.dumps({"status_code": "16000", "status_text": "获取总点赞成功", "result": result})
            else:
                return json.dumps({"status_code":"42000","status_text": "获取总点赞信息错误"})
        else:
            return json.dumps({"status_code": "42000", "status_text": "获取总点赞信息错误"})
@my_collection.route('/get_commets', methods=['POST'])
def get_comss():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = get_coms(i)
            if result:
                return json.dumps({"status_code": "16000", "status_text": "获取总点赞成功", "result": result})
            else:
                return json.dumps({"status_code":"42000","status_text": "获取总点赞信息错误"})
        else:
            return json.dumps({"status_code": "42000", "status_text": "获取总点赞信息错误"})
@my_collection.route('/get_coun', methods=['POST'])
def get_coun():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = get_count(i)
            if result:
                return json.dumps({"status_code": "16000", "status_text": "获取总点赞成功", "c": result})
            else:
                return json.dumps({"status_code":"42000","status_text": "获取总点赞信息错误"})
        else:
            return json.dumps({"status_code": "42000", "status_text": "获取总点赞信息错误"})
@my_collection.route('/get_coll', methods=['POST'])
def get_coll():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            # print(i)
            result = get_college(i)
            if result:
                return json.dumps({"status_code": "16000", "status_text": "获取总收藏成功", "c": result})
            else:
                return json.dumps({"status_code":"42000","status_text": "获取总收藏信息错误"})
        else:
            return json.dumps({"status_code": "42000", "status_text": "获取总收藏信息错误"})