from flask import Blueprint, request
from app.service.index_service import *
import json
index = Blueprint('index',__name__)


@index.route('/index_rande', methods=['GET', 'POST'])
def index_rande():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_rande = request.get_json()
            result = rande(index_rande)

            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})



# index开始
@index.route('/index_1', methods=['GET', 'POST'])
def index_1():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_1 = request.get_json()
            result = getpic1(index_1)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@index.route('/index_2', methods=['GET', 'POST'])
def index_2():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_2 = request.get_json()
            result = getpic2(index_2)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@index.route('/index_3', methods=['GET', 'POST'])
def index_3():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_3 = request.get_json()
            result = getpic3(index_3)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@index.route('/index_4', methods=['GET', 'POST'])
def index_4():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_4 = request.get_json()
            result = getpic4(index_4)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@index.route('/index_5', methods=['GET', 'POST'])
def index_5():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_5 = request.get_json()
            result = getpic5(index_5)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@index.route('/index_6', methods=['GET', 'POST'])
def index_6():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_6 = request.get_json()
            result = getpic6(index_6)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@index.route('/index_7', methods=['GET', 'POST'])
def index_7():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_7 = request.get_json()
            result = getpic7(index_7)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@index.route('/index_8', methods=['GET', 'POST'])
def index_8():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_8 = request.get_json()
            result = getpic8(index_8)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@index.route('/index_9', methods=['GET', 'POST'])
def index_9():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            index_9 = request.get_json()
            result = getpic9(index_9)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@index.route('/words_1', methods=['GET', 'POST'])
def words_1():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            words_1 = request.get_json()
            result = getwords1(words_1)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@index.route('/words_2', methods=['GET', 'POST'])
def words_2():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            words_2 = request.get_json()
            result = getwords2(words_2)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@index.route('/words_3', methods=['GET', 'POST'])
def words_3():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            words_3 = request.get_json()
            result = getwords3(words_3)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@index.route('/tj_1', methods=['GET', 'POST'])
def tj_1():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            tj_1 = request.get_json()
            result = get1(tj_1)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@index.route('/tj_2', methods=['GET', 'POST'])
def tj_2():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            tj_2 = request.get_json()
            result = get2(tj_2)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@index.route('/tj_3', methods=['GET', 'POST'])
def tj_3():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            tj_3 = request.get_json()
            result = get3(tj_3)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})