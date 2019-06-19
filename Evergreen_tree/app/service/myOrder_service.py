import app.dao.myOrder_dao as Orderdao


def get_order_detail_1(userid):
    if userid:
        result=Orderdao.get_order_detail(userid)
        return result
def del_order_detail_1(userid):
    if userid:
        result=Orderdao.del_order_detail(userid)
        return result
# if __name__ == '__main__':
#     a={"telephone":"18214890301"}
#     get_order_detail_1(a)