import app.dao.travellers_dao as travellersdao


def set_travellers_date(user_id):
    if user_id:
        result=travellersdao.set_travellers(user_id)
        return result
def get_travellers_date(purchaser_details):
    if purchaser_details:
        result=travellersdao.get_travellers(purchaser_details)
        return result