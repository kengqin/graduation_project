from flask import Blueprint, request,make_response
from app.service.comment_service import *
import json


comment = Blueprint('comment', __name__)


@comment.route('/comment', methods=['GET', 'POST'])
def my_comment():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            result = get_my_comment(i)
            print(result)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})
@comment.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            comment = select_my_comment(i)
            response=make_response()
            response.data=json.dumps({"status_code":"10600","status_text":"获取评论成功","comment":comment})
            if comment:
                return response
            else:
                return json.dumps({"status_code":"40600","status_text":"获取评论失败"})
        else:
            return json.dumps({"1102": "错误"})
@comment.route('/comment_del', methods=['GET', 'POST'])
def del_comment():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            comment = del_my_comment(i)
            response=make_response()
            response.data=json.dumps({"status_code":"10700","status_text":"删除成功","comment":comment})
            if comment:
                return response
            else:
                return json.dumps({"status_code":"40700","status_text":"获取评论失败"})
        else:
            return json.dumps({"1102": "错误"})
@comment.route('/comment_select', methods=['GET', 'POST'])
def comments_1():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            comment = select_my_comment_1(i)
            response=make_response()
            response.data=json.dumps({"status_code":"10800","status_text":"获取评论成功","comment":comment})
            if comment:
                return response
            else:
                return json.dumps({"status_code":"40800","status_text":"获取评论失败"})
        else:
            return json.dumps({"1102": "错误"})
@comment.route('/recipe_comment', methods=['POST'])
def recipe_comment():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            comment = select_recipe_comment(i)
            response=make_response()
            response.data=json.dumps({"status_code":"10801","status_text":"获取评论成功","comment":comment})
            if comment:
                return response
            else:
                return json.dumps({"status_code":"40800","status_text":"获取评论失败"})
        else:
            return json.dumps({"1102": "错误"})
@comment.route('/insert_recipe_comment', methods=['POST'])
def insert_recipe_comment():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            comment = insert_into_comments(i)
            response=make_response()
            response.data=json.dumps({"status_code":"11000","status_text":"评论成功"})
            if comment:
                return response
            else:
                return json.dumps({"status_code":"40800","status_text":"评论失败"})
        else:
            return json.dumps({"1102": "错误"})