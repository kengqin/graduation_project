import app.dao.sceipe_dao as sceipeDao
import json
from flask import make_response
def get_sceipe_first(res):
    res_sceipe_first = sceipeDao.select_sceipe_first(res)
    print(res_sceipe_first)
    if res_sceipe_first:
        response = make_response()
        response.data = json.dumps({"status_code": "10008",
                                    "status_text": "获取成功", "sceipe_first": res_sceipe_first})

        return response
def get_sceipe_first_1(res):
    res_sceipe_first = sceipeDao.select_sceipe_first_1(res)
    print(res_sceipe_first)
    if res_sceipe_first:
        response = make_response()
        response.data = json.dumps({"status_code": "10008",
                                    "status_text": "获取成功", "sceipe_first": res_sceipe_first})

        return response
def get_sceipe_first_name(res):
    res_sceipe_first = sceipeDao.select_sceipe_name(res)
    if res_sceipe_first:
        print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10009",
                                    "status_text": "获取成功", "name": res_sceipe_first['nickname']})

        return response

def get_sceipe_info(res):
    res_sceipe_first = sceipeDao.select_sceipe_info(res)
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10011",
                                    "status_text": "获取材料成功", "list" : res_sceipe_first})

        return response
def get_recipe_info(res):
    res_sceipe_first = sceipeDao.select_recipe_detail(res)
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10012",
                                    "status_text": "获取步骤成功", "list" : res_sceipe_first})

        return response


def get_recipe_infos(res):
    res_sceipe_first = sceipeDao.get_recipe_detail(res)
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10013",
                                    "status_text": "获取菜谱基本信息成功", "list" : res_sceipe_first})

        return response
def select_info():
    res_sceipe_first = sceipeDao.select_abll()
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10014",
                                    "status_text": "获取菜谱基本信息成功", "list" : res_sceipe_first})

        return response
def select_info_point(res):
    res_sceipe_first = sceipeDao.select_point(res)
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10015",
                                    "status_text": "搜索获取菜谱基本信息成功", "list" : res_sceipe_first})

        return response
    else:
        return json.dumps({'status_code':"40001","status_text":"没有查询结果"})
def select_self_counter(res):
    res_sceipe_first = sceipeDao.select_self(res)
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10016",
                                    "status_text": "获取点赞菜谱基本信息成功", "list": res_sceipe_first})

        return response
    else:
        return json.dumps({'status_code':"40002","status_text":"没有点赞记录"})

def select_self_college(res):
    res_sceipe_first = sceipeDao.select_selfcollge(res)
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10017",
                                    "status_text": "获取收藏菜谱基本信息成功", "list": res_sceipe_first})

        return response
    else:
        return json.dumps({'status_code':"40003","status_text":"没有收藏记录"})

def get_nickname_recipe(res):
    res_sceipe_first = sceipeDao.get_nickname(res)
    if res_sceipe_first:
        # print(res_sceipe_first)
        response = make_response()

        response.data = json.dumps({"status_code": "10018",
                                    "status_text": "获取菜谱nickname成功", "list": res_sceipe_first})
        return response
    else:
        return json.dumps({'status_code':"40003","status_text":"没有找到"})
# if __name__ == '__main__':
#     res={'user_id': 5}
#     select_self_counter(res)