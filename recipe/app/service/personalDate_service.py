import app.dao.personalDate_dao as personaldao


def get_personal_Date(user_id):
    # print(user_id)
    if user_id:
        result=personaldao.get_personal_date(user_id)
        # print(result)
        return result


def change_personal_Date(user_id):
    if user_id:
        result=personaldao.change_personal_date(user_id)
        # print(result)
        return result
# if __name__ == '__main__':
#     a = {"telephone": 18792031925}
#     get_personal_Date(a)