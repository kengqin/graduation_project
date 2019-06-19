from flask import Blueprint, request
# 导入user service模块

from app.service.user_service import *
import json


# 用参数name和import_name初始化
# user是模块的名称
user = Blueprint('user', __name__)


# restful api
@user.route('/users')
def users():
    return 'welcome user page!!'


@user.route('/person', methods=['POST', 'GET', 'PUT', 'DELETE'])
def person():
    if request.method == 'GET':
        return '获取用户信息'
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            u = request.get_json()
            print(u)
            # result为添加用户的结果
            result = addUser(u)
            return result
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    elif request.method == 'PUT':
        return '修改用户'
    elif request.method == 'DELETE':
        return '删除用户'


@user.route('/login', methods=['POST'])
def login():
    if request.is_json and request.get_json():
        u = request.get_json()
        result = getUserById(u)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

@user.route('/admin_login',methods=['POST'])
def admin_login():
    if request.is_json and request.get_json():
        u = request.get_json()
        result = getAdminById(u)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


@user.route('/userinfo',methods=['POST'])
def get_userinfo():
    if request.is_json and request.get_json():
        u = request.get_json()
        result = select_userinfo(u)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
@user.route('/update_userinfo',methods=['POST'])
def update_userinfos():
    if request.is_json and request.get_json():
        u = request.get_json()
        print(u)
        result = update_userinfo(u)
        return result

# 七牛云token
@user.route('/upload',methods=['POST'])
def qiniuToken():
    from qiniu import Auth
    import uuid
    if request.is_json and request.get_json():
        obtain = request.get_json()
        try:
            if obtain.get('iconname'):
                # 需要填写你的 Access Key 和 Secret Key
                access_key = 'S6vahXeUOO9XYVOFmQCA6DUEogcWmC-ijbtZHGIl'
                secret_key = 'Cn4ep15dHJcDI_oWuSvVMRWoGI4CmWV2GGBZSRDY'
                # 构建鉴权对象
                q = Auth(access_key, secret_key)
                # 要上传的空间
                bucket_name = 'image'
                domain = 'http://prurxs7re.bkt.clouddn.com'
                # 上传头像
                # 上传到七牛后保存的文件名
                filename = str(uuid.uuid4()) + '.' + obtain['iconname'].split('.')[1]
                # 生成上传 Token，可以指定过期时间等
                token = q.upload_token(bucket_name, filename, 3600)
                response = make_response()

                response.data=json.dumps({"status_code": "20000", "status_text": "请求成功", "qiniu_token": token, "filename": filename,
                     "domain": domain})
                return response
            else:
                return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
        except Exception as ex:
            print('七牛云token错误')
            print(ex)
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    else:
        return json.dumps({"status_code": "40000", "status_text": "请求方法不合法"})
@user.route('/insert_recipeinfo',methods=['POST'])
def insert_recipeinfo():
    if request.is_json and request.get_json():
        u = request.get_json()
        print(u)
        result = insert_recipes(u)
        return result
@user.route('/insert_details',methods=['POST'])
def insert_details():
    if request.is_json and request.get_json():
        u = request.get_json()
        # print(u)
        result = insert_detai(u)
        return result
@user.route('/select_recipes',methods=['POST'])
def select_recipess():
    if request.is_json and request.get_json():
        u = request.get_json()
        # print(u)
        result = recipe_select(u)
        return result
@user.route('/delete_recipes',methods=['POST'])
def delete_recipess():
    if request.is_json and request.get_json():
        u = request.get_json()
        # print(u)
        result = recipe_delete(u)
        return result
@user.route('/select_alluser',methods=['GET'])
def select_alluser():
    result = user_get()
    return result

@user.route('/select_userinfo',methods=['POST'])
def select_user():
    if request.is_json and request.get_json():
        u = request.get_json()
        result = user_se(u)
        return result

@user.route('/updates',methods=['POST'])
def updates():
    if request.is_json and request.get_json():
        u = request.get_json()
        print(u)
        result = user_update(u)
        return result
@user.route('/selet_info',methods=['POST'])
def selet_info():
    if request.is_json and request.get_json():
        u = request.get_json()
        print(u)
        result = user_sele(u)
        return result