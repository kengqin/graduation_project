from flask import Blueprint, request,make_response
from app.service.scenic_service import *
import json

detail = Blueprint('detail', __name__)




@detail.route('/details', methods=['GET', 'POST'])
def person():
    if request.method == 'GET':
        return 'loding'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            i = request.get_json()
            result = getdatabyid(i)
            return json.dumps(result)
        else:
            return json.dumps({"1102": "错误"})

@detail.route('/detailss', methods=['GET', 'POST'])
def words1():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            i1 = request.get_json()
            result = getdatabyid2(i1)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@detail.route('/address',methods=['GET', 'POST'])
def address():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            adress = request.get_json()
            result = getdatabyid3(adress)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@detail.route('/open_time',methods=['GET', 'POST'])
def time():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            time = request.get_json()
            result = getdatabyid4(time)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@detail.route('/adult_price',methods=['GET', 'POST'])
def adult_price():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            adult_price = request.get_json()
            # print(adult_price)
            result = getdatabyid5(adult_price)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@detail.route('/ticket',methods=['GET', 'POST'])
def ticket():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            ticket = request.get_json()
            result = getdatabyid6(ticket)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})



@detail.route('/market_value', methods=['GET', 'POST'])
def market_value():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            market_value = request.get_json()
            result = getdatabyid13(market_value)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@detail.route('/image_ponit', methods=['GET', 'POST'])
def image_ponit():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            image_ponit = request.get_json()
            result = getdatabyid14(image_ponit)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@detail.route('/image_ad1', methods=['GET', 'POST'])
def image_ad1():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            image_ad1 = request.get_json()
            result = getdatabyid15(image_ad1)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})

@detail.route('/image_ad2', methods=['GET', 'POST'])
def image_ad2():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            image_ad2 = request.get_json()
            result = getdatabyid16(image_ad2)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})




@detail.route('/getid', methods=['GET', 'POST'])
def gid():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            gid = request.get_json()

            result = uid(gid)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})




@detail.route('/col_id', methods=['GET', 'POST'])
def gd():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            gd = request.get_json()

            result = getnewid1(gd)
            if result:
                response = make_response()
                response.data = json.dumps({"status_code": "10111", "status_text": "已收藏","result":result})
                return response
            else:
                return json.dumps({"status_code":"40111","status_text":"未收藏"})



@detail.route('/into', methods=['GET', 'POST'])
def into():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            into = request.get_json()

            result = io(into)

            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})




@detail.route('/sc', methods=['GET', 'POST'])
def sc():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            sc = request.get_json()
            result = shanchu(sc)
            return json.dumps(result)
        else:
            return json.dumps({"1102":"错误"})


@detail.route('/select_comment', methods=['GET', 'POST'])
def select():
    if request.method=='GET':
        return 'loding'
    elif request.method=='POST':
        if request.is_json and request.get_json():
            sc = request.get_json()
            result = comment_select(sc)
            response=make_response()
            # print(response)
            if result:
                response.data=json.dumps({"status_code":"10500","status_text":"评论获取成功","comment":result})
                return response
            else:
                return json.dumps({"status_code":"40500","status_text":"暂无评论!"})
        else:
            return json.dumps({"1102":"错误"})


