import app.dao.search_dao as userdao
import json


def search1(id):
    if id:
        search1 = userdao.search1(id)
        return search1

def search2(id):
    if id:
        search2 = userdao.search2(id)

        return search2

def search3(id):
    if id:
        search3 = userdao.search3(id)

        return search3


# if __name__ == '__main__':
#     s = {"tname": "苏州"}
#     search2(s)

