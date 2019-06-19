import app.dao.purchaser_dao as purchaserdao


def get_my_purchaser(user_id):
    if user_id:
        result=purchaserdao.get_purchaser(user_id)
        return result
def set_my_purchaser(purchaser_details):
    if purchaser_details:
        result=purchaserdao.set_purchaser(purchaser_details)
        return result