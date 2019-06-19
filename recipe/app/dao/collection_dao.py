# 导入连接池  用连接池创建链接
from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_collection import sql_mycollection
import json





def get_my_collection(user_id):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('get_my_collection').format(telephone=user_id['telephone'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchall()#获取返回的数据  只取一条
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data

def del_my_collection(collect_id):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('del_my_collection').format(id=collect_id['id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchall()#获取返回的数据  只取一条
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def select_recipe_collection(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('select_college').format(recipe_id=res['recipe_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def select_recipe_counter(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('select_counter').format(recipe_id=res['recipe_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        print(res_data)
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def select_college_on(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('select_college_on').format(recipe_id=res['recipe_id'],user_id=res['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        print(res_data)
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def insert_college_on(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('insert_into_college').format(recipe_id=res['recipe_id'],user_id=res['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = int(cursor.lastrowid)#获取返回的数据  只取一条
        print(res_data)
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def delete_college_on_2(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('delete_college').format(recipe_id=res['recipe_id'],user_id=res['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data =int(cursor.lastrowid)#获取返回的数据  只取一条
        re=res_data if res_data else None
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return re


def select_counter_on_1(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('select_counter_on').format(recipe_id=res['recipe_id'],user_id=res['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data=cursor.fetchone()
        # res_data=int(cursor.lastrowid)#获取返回的数据  只取一条
        print(res_data)
        # re=res_data if res_data else None
        # print(re)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def insert_counter_on(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('insert_into_counter').format(recipe_id=res['recipe_id'],user_id=res['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = int(cursor.lastrowid)#获取返回的数据  只取一条
        print(res_data)
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def delete_counter_on_2(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('delete_counter').format(recipe_id=res['recipe_id'],user_id=res['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = int(cursor.lastrowid)#获取返回的数据  只取一条
        re=res_data if res_data else None
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return re

def select_user_count(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('user_counts').format(recipe_id=res['recipe_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        print(res_data)
        re=res_data if res_data else None
        print(re)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return re
def select_user_college(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('user_colleges').format(recipe_id=res['recipe_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        print(res_data)
        re=res_data if res_data else None
        print(re)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return re
def get_comms(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('get_comments').format(recipe_id=res['recipe_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        print(res_data)
        re=res_data if res_data else None
        # print(re)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return re
def user_count(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('user_coun').format(recipe_id=res['recipe_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchall()#获取返回的数据  只取一条
        print(res_data)
        res=0
        for i in res_data:
            # print(i)
            sql1=sql_mycollection.get('select_counter').format(recipe_id=i['id'])
            # print(sql1)
            cursor.execute(sql1)
            re=cursor.fetchone()
            # print(re)
            res +=re['counter']
            # print(res)
            re=res if res else None
        print(re)

        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return re
def user_colleg(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mycollection.get('user_coun').format(recipe_id=res['recipe_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchall()#获取返回的数据  只取一条
        print(res_data)
        res=0
        for i in res_data:
            # print(i)
            sql1=sql_mycollection.get('select_college').format(recipe_id=i['id'])
            # print(sql1)
            cursor.execute(sql1)
            re=cursor.fetchone()
            # print(re)
            res +=re['college']
            # print(res)
            re=res if res else None
        print(re)

        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return re
# if __name__ == '__main__':
#     res={"recipe_id":8}
#     user_colleg(res)