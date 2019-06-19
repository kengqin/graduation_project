import app.dao.scenic_dao as userdao
import json

def getdatabyid(id):
    if id:
        rr=userdao.getdatabyid(id)
        return rr
def getdatabyid2(id):
    if id:
        a=userdao.getdatabyid2(id)
        return a

def getdatabyid3(id):
    if id:
        b = userdao.getdatabyid3(id)
        return b

def getdatabyid4(id):
    if id:
        c = userdao.getdatabyid4(id)
        return c

def getdatabyid5(id):
    if id:
        d = userdao.getdatabyid5(id)

        return d

def getdatabyid6(id):
    if id:
        e = userdao.getdatabyid6(id)
        return e



def getdatabyid13(id):
    if id:
        l = userdao.getdatabyid13(id)
        return l

def getdatabyid14(id):
    if id:
        m = userdao.getdatabyid14(id)
        return m

def getdatabyid15(id):
    if id:
        n = userdao.getdatabyid15(id)
        return n

def getdatabyid16(id):
    if id:
        ad2 = userdao.getdatabyid16(id)
        return ad2

def uid(id):
    if id:
        u_id = userdao.uid(id)
        return u_id

def io(id):
    if id:
        idd=userdao.into(id)
        return idd

def getnewid1(id):
    if id:
        nid=userdao.getnewid1(id)

        return nid

def shanchu(id):
    if id:
        sdd=userdao.shanchu(id)
        return sdd
def comment_select(res):
    if res:
        a=userdao.select_comment(res)
        # print(a)
        return a
# if __name__ == '__main__':
#     s={"scenic_id":1}
#     comment_select(s)