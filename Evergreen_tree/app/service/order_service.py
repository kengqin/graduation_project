import app.dao.order_dao as orderDao
import json
from flask import make_response

def get_ticket_info(res):
    res_order = orderDao.get_ticket(res)

    if res_order:
        response = make_response()
        response.data = json.dumps({"status_code": "10008",
                                    "status_text": "获取成功", "tname": res_order[0]['tname'], "adult_introduce":res_order[0]['adult_introduce'], "adult_price":res_order[0]['adult_price']})

        return response


def create_order(res):
    # print(res)
    res_buy=orderDao.order_create(res)
    # print(res_buy)
    if res_buy:
        response = make_response()
        response.data = json.dumps({"status_code": "10009",
                                    "status_text": "获取成功", "id": res_buy})
        return response

def get_order_id_info(res):
    ress = orderDao.get_info(res)
    if ress:
        return ress

def order_update(res):
    r=orderDao.update_order(res)
    if r:
        return r
def order_select(res):
    r=orderDao.select_order(res)
    if r:
        return r
# if __name__ == '__main__':
#     # user = {
#     #     "order_id": "201902161512720", "scenic_id": 1,
#     #     "tourst_time": "2019-2-16", "onum": 4, "oname":"唐扬", "otelephone": "18792031925", "order_start": 1,
#     #     "telephone":"18792031925"
#     # }
#     user={
#         "order_id":"201902201702110"
#     }
#     # print(user)
#     order_select(user)