from flask import Blueprint, request
# 导入user service模块

from app.service.sceipe_service import *
import json

# 用参数name和import_name初始化
# user是模块的名称
sceipe = Blueprint('sceipe', __name__)


@sceipe.route('/sceipe_first', methods=['GET'])
def sceipe_first():
    u = request.get_json()
    result = get_sceipe_first(u)
    return result
@sceipe.route('/sceipe_first_1', methods=['GET'])
def sceipe_first_1():
    u = request.get_json()
    result = get_sceipe_first_1(u)
    return result

@sceipe.route('/sceipe_first_name', methods=['POST'])
def sceipe_first_name():
    u = request.get_json()
    result = get_sceipe_first_name(u)
    return result

@sceipe.route('/get_sceipeinfo', methods=['POST'])
def get_sceipeinfos():
    u = request.get_json()
    result = get_sceipe_info(u)
    return result

@sceipe.route('/get_sceipedetail', methods=['POST'])
def get_sceipedatails():
    u = request.get_json()
    result = get_recipe_info(u)
    return result
@sceipe.route('/get_sceipedetailinfo', methods=['POST'])
def get_sceipedatailinfo():
    u = request.get_json()
    result = get_recipe_infos(u)
    return result

@sceipe.route('/get_allinfo', methods=['GET'])
def get_allinfo():
    u = request.get_json()
    result = select_info()
    return result
@sceipe.route('/get_info_point', methods=['POST'])
def get_info_point():
    u = request.get_json()
    result = select_info_point(u)
    return result

@sceipe.route('/get_self', methods=['POST'])
def get_self_reicpe():
    u = request.get_json()
    result = select_self_counter(u)
    return result

@sceipe.route('/get_selfcollege', methods=['POST'])
def get_selfcoll():
    u = request.get_json()
    result = select_self_college(u)
    return result

@sceipe.route('/get_nickname', methods=['POST'])
def get_nick():
    u = request.get_json()
    result = get_nickname_recipe(u)
    return result