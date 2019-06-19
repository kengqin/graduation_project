# 导入连接池  用连接池创建链接
from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_comment import sql_comment
import datetime
import json





def get_comment(user_id):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_comment.get('get_comment').format(user_id=user_id['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchall()#获取返回的数据  只取一条
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def select_comment(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_comment.get('select_comment').format(telephone=res['telephone'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchall()#获取返回的数据  只取一条
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def del_comment(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_comment.get('del_comment').format(order_id=res['order_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res = cursor.fetchall()  # 获取返回的数据  只取一条
        res_data = res if res else -1
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def comment_se(res):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_comment.get('comment_se').format(order_id=res['order_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data

# 查询评论
def insert_recipe_comment(res):
    try:
        res_data = None  # 定义返回值
        # re = None
        # res_su = None
        # time=None
        client=POOL.connection()#链接池创建链接
        # today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # print(today_date)
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql=sql_comment.get("get_sceipe_comment").format(recipe_id=res['recipe_id'])
        cursor.execute(sql)
        res_data=cursor.fetchall()
        print(res_data)
        # res_su = int(cursor.lastrowid)#获取返回的数据  只取一条

        # print(res_data)
        # print(res_su)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
        print(ex)
    finally:
        client.close()
        return res_data
def insert_into_comment(res):
    try:
        res_data = None  # 定义返回值
        # re = None
        # res_su = None
        # time=None
        client=POOL.connection()#链接池创建链接
        today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(today_date)
        print(res)
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql=sql_comment.get("insert_sceipe_comment").format(user_id=res['user_id'],comm=res['comm'],comment_time=today_date,recipe_id=res['recipe_id'])
        cursor.execute(sql)
        # res_data=cursor.fetchall()
        # print(res_data)
        res_data = int(cursor.lastrowid)#获取返回的数据  只取一条

        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
        print(ex)
    finally:
        client.close()
        return res_data
# if __name__ == '__main__':
#     a={"recipe_id":6}
#     insert_recipe_comment(a)