from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_sceipe import sql_sceipe
def select_sceipe_first(id):
    try:
        client=POOL.connection()
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('select_sceipe_height')

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_sceipe
def select_sceipe_first_1(id):
    try:
        client=POOL.connection()
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('select_sceipe_height_1')

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_sceipe
def select_sceipe_name(id):
    try:
        client=POOL.connection()
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('select_user_name').format(id=id['id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchone()
        print(res_sceipe)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_sceipe

def select_sceipe_info(res):
    try:
        client=POOL.connection()
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('select_sceipe_info').format(recipe_id=res['recipe_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        print(res_sceipe)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_sceipe
def select_recipe_detail(res):
    try:
        client=POOL.connection()
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('select_recipe_detail').format(recipe_id=res['recipe_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        print(res_sceipe)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_sceipe
def get_recipe_detail(res):
    try:
        client=POOL.connection()
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('get_recipe_info').format(recipe_id=res['recipe_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        print(res_sceipe)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_sceipe
def select_abll():
    try:
        client=POOL.connection()
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('search_sceipe')

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        print(res_sceipe)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return res_sceipe

def select_point(res):
    try:
        client=POOL.connection(res)
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('search_recipe').format(select=res['select'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        re=res_sceipe if res_sceipe else None
        print(re)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return re
def select_self(res):
    try:
        client=POOL.connection(res)
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('select_self').format(user_id=res['user_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        re=res_sceipe if res_sceipe else None
        print(re)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return re
def select_selfcollge(res):
    try:
        client=POOL.connection(res)
        res_sceipe = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('select_selfcollege').format(user_id=res['user_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchall()
        re=res_sceipe if res_sceipe else None
        print(re)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return re

def get_nickname(res):
    try:
        client=POOL.connection(res)
        res_sceipe = None
        re=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_sceipe.get('get_nickname').format(recipe_id=res['recipe_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_sceipe = cursor.fetchone()
        re=res_sceipe if res_sceipe else None
        print(re)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        # print(res_user)
        return re
# if __name__ == '__main__':
#     res={'recipe_id': 6}
#     get_nickname(res)
