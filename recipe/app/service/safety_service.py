import app.dao.safety_dao as safetydao


def chechk_info(user_id):
    if user_id:
        result=safetydao.get_safety_info(user_id)
        return result
