import app.dao.comment_dao as commentdao


def get_my_comment(user_id):
    if user_id:
        result=commentdao.get_comment(user_id)
        return result

def select_my_comment(user_id):
    if user_id:
        result=commentdao.select_comment(user_id)
        return result
def del_my_comment(user_id):
    if user_id:
        result=commentdao.del_comment(user_id)
        return result
def select_my_comment_1(user_id):
    if user_id:
        result=commentdao.comment_se(user_id)
        return result
def select_recipe_comment(user_id):
    if user_id:
        result=commentdao.insert_recipe_comment(user_id)
        return result
def insert_into_comments(res):
    if res:
        result=commentdao.insert_into_comment(res)
        if result:
            return result

# if __name__ == '__main__':
#     a={"recipe_id":6}
#     select_recipe_comment(a)