import app.dao.collection_dao as collectiondao


def get_my_collection(user_id):
    if user_id:
        result=collectiondao.get_my_collection(user_id)
        return result
def del_my_collection(collect_id):
    if collect_id:
        result=collectiondao.del_my_collection(collect_id)
        return result

# 获取收藏数
def select_my_collection(res):
    if res:
        result=collectiondao.select_recipe_collection(res)
        return result
# 获取点赞数
def select_my_counter(res):
    if res:
        result=collectiondao.select_recipe_counter(res)
        return result
def select_college_on_1(res):
    if res:
        result=collectiondao.select_college_on(res)
        return result
def insert_college_on_1(res):
    if res:
        result=collectiondao.insert_college_on(res)
        return result
def delete_college_on_1(res):
    if res:
        result=collectiondao.delete_college_on_2(res)
        return result

def select_counter_on_2(res):
    if res:
        result=collectiondao.select_counter_on_1(res)
        return result
def insert_counter_on_1(res):
    if res:
        result=collectiondao.insert_counter_on(res)
        return result
def delete_counter_on_1(res):
    if res:
        result=collectiondao.delete_counter_on_2(res)
        return result
def select_uer_count(res):
    if res:
        result=collectiondao.select_user_count(res)
        return result
def select_uer_college(res):
    if res:
        result=collectiondao.select_user_college(res)
        return result
def get_coms(res):
    if res:
        result=collectiondao.get_comms(res)
        return result
def get_count(res):
    if res:
        result=collectiondao.user_count(res)
        return result
def get_college(res):
    if res:
        result=collectiondao.user_colleg(res)
        return result
# if __name__ == '__main__':
#     a={"recipe_id":6}
#     select_my_counter(a)
# if __name__ == '__main__':
#     a={"recipe_id":6,"user_id":4}
#     insert_counter_on_1(a)
# if __name__ == '__main__':
#     res={"recipe_id":6}
#     select_uer_count(res)
if __name__ == '__main__':
    res={"recipe_id":8}
    get_count(res)