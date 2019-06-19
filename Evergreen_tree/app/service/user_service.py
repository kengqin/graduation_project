import app.dao.user_dao as userDao
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask import make_response
from app.utils.my_token import createToken


def addUser(user):
    if user.get('telephone') and user.get('password'):

        pf = generate_password_hash(user['password'], method='pbkdf2:sha1:1001', salt_length=8)
        user['password'] = pf
        rr = userDao.addUser(user)
        aa = userDao.getUserById(user['telephone'])
        if rr:
            if rr == -1:
                return json.dumps({"status_code": "10002", "status_text": "用户已经存在"})
            else:
                token = createToken(user['telephone'])
                response = make_response()
                response.data = json.dumps({"status_code": "10001",
                                            "status_text": "注册成功", "token": token, "user_id": rr,
                                            'nickname': aa['nickname']})
                return response
        else:
            print(rr)
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


def getUserById(user):
    res_user = userDao.getUserById(user['telephone'])
    if res_user:
        if res_user == -1:
            # print("m")
            return json.dumps({"status_code": "10004", "status_text": "该用户不存在"})
        else:
            # 验证密码是否相同
            if (check_password_hash(res_user['password'], user['password'])):
                # 构建token

                token = createToken(user['telephone'])
                # return json.dumps({"status_code":"10003","status_text":"登录成功"}),200,{"token":token}

                response = make_response()
                # print("b")
                response.data = json.dumps({"status_code": "10003",
                                            "status_text": "登录成功", "token": token, "user_id": res_user['id'],
                                            "nickname": res_user["nickname"]})
                # 此处前端ajax无法获取header所以这种方式不可行
                # response.headers['token']=token
                response.status_code = 200
                return response
            else:
                # print("c")
                return json.dumps({"status_code": "10005", "status_text": "密码错误"})
    else:
        # print("a")
        # print(res_user)
        return json.dumps({"status_code": "10004", "status_text": "该用户不存在"})


def updateUser(user):
    pass


def deleteUserById(id):
    pass


def login(user):
    pass


def getAdminById(user):
    res_user = userDao.getAdminById(user['telephone'])
    if res_user:
        if res_user == -1:
            print("m")
            return json.dumps({"status_code": "10004", "status_text": "该管理员不存在"})
        else:
            # 验证密码是否相同
            if res_user['password'] == user['password']:
                # 构建token

                # token = createToken(user['telephone'])
                # # return json.dumps({"status_code":"10003","status_text":"登录成功"}),200,{"token":token}

                response = make_response()
                # print("b")
                response.data = json.dumps({"status_code": "10003",
                                            "status_text": "登录成功", "id": res_user['id'], "role": res_user["role"],
                                            'telephone': res_user['telephone']})
                # 此处前端ajax无法获取header所以这种方式不可行
                # response.headers['token']=token
                response.status_code = 200
                return response
            else:
                # print("c")
                return json.dumps({"status_code": "10005", "status_text": "管理员密码错误"})
    else:
        print("a")
        # print(res_user)
        return json.dumps({"status_code": "10004", "status_text": "该管理员不存在"})


def select_userinfo(user):
    res_user = userDao.select_user(user)
    if res_user:
        print(res_user)

        response = make_response()
        response.data = json.dumps({"status_code": "10004",
                                    "status_text": "获取用户信息成功", "id": res_user})
        return response


def update_userinfo(user):
    res_user = userDao.update_user(user)
    # print(res_user)
    response = make_response()
    response.data = json.dumps({"status_code": "10004",
                                "status_text": "修改用户信息成功", "res": res_user})
    return response

def insert_recipes(user):
    res_user = userDao.inset_detail(user)
    if res_user:
        response = make_response()
        response.data = json.dumps({"status_code": "10004",
                                    "status_text": "上传食谱成功", "result": res_user})
        return response
    else:
        return json.dumps({"status_code": "400",
                                "status_text": "上传失败"})
def insert_detai(user):
    res= userDao.insert_detail(user)
    if res:
        response = make_response()
        response.data = json.dumps({"status_code": "10004",
                                    "status_text": "上传食谱成功", "result": res})
        return response
    else:
        return json.dumps({"status_code": "400",
                                "status_text": "上传失败"})
def recipe_select(user):
    res= userDao.select_recipe(user)
    if res:
        response = make_response()
        response.data = json.dumps({"status_code": "10004",
                                    "status_text": "查询食谱成功", "list": res})
        return response
    else:
        return json.dumps({"status_code": "400",
                                "status_text": "获取用户所有食谱失败"})
def recipe_delete(user):
    res= userDao.delete_recipe(user)
    if res:
        response = make_response()
        response.data = json.dumps({"status_code": "10004",
                                    "status_text": "删除食谱成功"})
        return response
    else:
        return json.dumps({"status_code": "400",
                                "status_text": "删除食谱失败"})
def user_get():
    res= userDao.get_alluser()
    if res:
        response = make_response()
        response.data = json.dumps({"status_code": "10004",
                                    "status_text": "获取用户信息成功",'list':res})
        return response
    else:
        return json.dumps({"status_code": "400",
                                "status_text": "获取用户信息失败"})
def user_se(res):
    res= userDao.select_info(res)
    if res:
        response = make_response()
        response.data = json.dumps({"status_code": "10004",
                                    "status_text": "获取用户信息成功",'list':res})
        return response
    else:
        return json.dumps({"status_code": "400",
                                "status_text": "获取用户信息失败"})

def user_update(user):
    res_user = userDao.update_info(user)
    # print(res_user)
    response = make_response()
    response.data = json.dumps({"status_code": "10004",
                                "status_text": "修改用户信息成功", "res": res_user})
    return response

def user_sele(user):
    res_user = userDao.sele_info(user)
    # print(res_user)
    response = make_response()
    response.data = json.dumps({"status_code": "10004",
                                "status_text": "查询用户信息成功", "list": res_user})
    return response
# if __name__ == '__main__':
#     user = { "user_id": 3}
#     select_userinfo(user)
# if __name__ == '__main__':
#     user = {"telephone": "13812790420", "password": "123456"}
#     addUser(user)
