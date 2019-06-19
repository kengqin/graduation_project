# 用户模块
from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_user import sql_user
import time

# 注册用户
def addUser(user):
    '''
    :param user:
    :return: 返回注册成功后用户的id；如果id为None说明注册失败，id如果为0表示该用户已经存在，id为1表示注册成功
    '''

    if not getUserById(user['telephone']):
        try:
            client = POOL.connection()
            user_id = None
            cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
            # 4. 准备sql语句
            # sql = 'insert into user(telephone,password,regist_date) ' \
            #       'values("{telephone}","{password}",CURDATE())'. \
            #     format(telephone=user['telephone'], password=user['password'])

            sql = sql_user.get('addUser').format(telephone=user['telephone'], password=user['password'],nickname=user['nickname'])
            # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
            cursor.execute(sql)
            user_id = int(cursor.lastrowid)
            client.commit()
        except Exception as ex:
            client.rollback()
        finally:
            return user_id
    else:
        return -1


def getUserById(id):
    try:
        client=POOL.connection()
        res_user = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_user.get('getUserById').format(
            telephone=id)

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_user = cursor.fetchone()

        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user


def getAdminById(id):
    try:
        client=POOL.connection()
        res_user = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_user.get('getAdminById').format(telephone=id)

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_user = cursor.fetchone()

        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user
def select_user(id):
    try:
        client=POOL.connection()
        res_user = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_user.get('select_uer').format(id=id["user_id"])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_user = cursor.fetchone()
        print(res_user)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user

def update_user(res):
    try:
        client=POOL.connection()
        res_user = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        print(res)
        # 4. 准备sql语句
        sql = sql_user.get('update_user').format(nickname=res['nickname'],email=res['email'],name=res['name'],qq=res['qq'],sex=res['sex'],age=res['age'],id=res['user_id'])
        print(sql)
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_user = int(cursor.lastrowid)
        print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user
def inset_detail(res):
    try:
        client=POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        res_user=insert_recipe(res)
        # 4. 准备sql语句
        print(res_user)
        sql1 = sql_user.get('insert_detail').format(recipe_id=int(res_user), src=res['src'], describes=res['describes'])
        cursor.execute(sql1)
        # a = int(cursor.lastrowid)
        # print(a)

        sql2=sql_user.get('insert_make').format(step=res['step'],recipe_id=int(res_user))
        cursor.execute(sql2)
        # b=int(cursor.lastrowid)
        # print(b)
        for a in res['listItem']:

            sql3=sql_user.get('insert_ingredients').format(recipe_id=int(res_user),ingredients=a['ingredients'],amount=a['amount'])
            cursor.execute(sql3)
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        print(res_user)
        res=1
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res

def insert_recipe(res):
    try:
        client=POOL.connection()
        res_user=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('insert_recipe').format(rname=res['rname'],user_id=int(res['user_id']),src=res['src'])
        cursor.execute(sql)
        res_user = int(cursor.lastrowid)
        # print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user
def insert_detail(res):
    try:
        client=POOL.connection()
        res_user=True
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('insert_detail').format(recipe_id=int(res['recipe_id']), src=res['src'], describe=res['describe'])
        cursor.execute(sql)
        res_user = int(cursor.lastrowid)
        # print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user
def select_recipe(res):
    try:
        client=POOL.connection()
        res_user=True
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('select_recipe').format(user_id=res['user_id'])
        cursor.execute(sql)
        res_user = cursor.fetchall()
        # print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user
def delete_recipe(res):
    try:
        client=POOL.connection()
        res_user=True
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('delete_make').format(recipe_id=res['recipe_id'])
        cursor.execute(sql)
        sql1 = sql_user.get('delete_ingredients').format(recipe_id=res['recipe_id'])
        cursor.execute(sql1)
        sql2 = sql_user.get('delete_detail').format(recipe_id=res['recipe_id'])
        cursor.execute(sql2)
        sql4 = sql_user.get('delete_college').format(recipe_id=res['recipe_id'])
        cursor.execute(sql4)
        sql5 = sql_user.get('delete_counter').format(recipe_id=res['recipe_id'])
        cursor.execute(sql5)
        sql6 = sql_user.get('delete_comment').format(recipe_id=res['recipe_id'])
        cursor.execute(sql6)
        sql3 = sql_user.get('delete_recipe').format(recipe_id=res['recipe_id'])
        cursor.execute(sql3)
        # print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user
def get_alluser():
    try:
        client=POOL.connection()
        res_user=True
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('select_alluser')
        cursor.execute(sql)
        res_user = cursor.fetchall()
        # print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user

def select_info(res):
    try:
        client=POOL.connection()
        res_user=True
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('select_userinfo').format(user_id=res['user_id'])
        cursor.execute(sql)
        res_user = cursor.fetchall()
        print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user

def update_info(res):
    try:
        client=POOL.connection()
        res_user = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        print(res)
        # 4. 准备sql语句
        sql = sql_user.get('update_userinfo').format(nickname=res['nickname'],name=res['name'],telephone=res['telephone'],sex=res['sex'],id=res['user_id'])
        print(sql)
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_user = int(cursor.lastrowid)
        print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user

def sele_info(res):
    try:
        client=POOL.connection()
        res_user = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        print(res)
        # 4. 准备sql语句
        sql = sql_user.get('select_adm').format(id=res['user_id'])
        print(sql)
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_user=cursor.fetchone()
        print(res_user)
        # res=res_user if res_user else None
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_user
# if __name__ == '__main__':
#     use = {'rname': '中餐', 'describes': '市场的', 'step': '反反复复烦烦烦烦烦烦烦烦烦烦烦烦烦烦烦', 'listItem': [{'ingredients': '1', 'amount': '1'}, {'ingredients': '2', 'amount': '2'}], 'src': 'http://prurxs7re.bkt.clouddn.com/e95faf63-78f7-445b-9115-144a83cf21b0.jpg', 'user_id': '3'}
#
#     inset_detail(use)
if __name__ == '__main__':
    res={"user_id":'王'}
    select_info(res)

