# 导入连接池  用连接池创建链接
from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_mydetails import sql_mydetails
import json
import datetime





def get_order_mydetail(order_id):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_mydetails.get('get_order_detail').format(order_id=order_id['order_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchall()#获取返回的数据  只取一条
        # print(res_data)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data
def insert_order_mydetail(res):
    try:
        res_data = None  # 定义返回值
        re = None
        res_su = None
        # time=None
        client=POOL.connection()#链接池创建链接
        today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # print(today_date)
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql1=sql_mydetails.get("select_user_id").format(telephone=res['telephone'])
        cursor.execute(sql1)
        re=cursor.fetchone()
        # print(re)
        sql2=sql_mydetails.get('insert_comment').format(order_id=res['order_id'],user_id=re['id'],comm=res['content'],comment_time=today_date,scenic_id=res['scenic_id'])
        cursor.execute(sql2)  # 执行sql语句
        res_data = int(cursor.lastrowid)
        # print(res_data)
        sql = sql_mydetails.get('update_order_ticket').format(order_id=res['order_id'],order_start=res['order_start'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_su = int(cursor.lastrowid)#获取返回的数据  只取一条

        # print(res_data)
        # print(res_su)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
        print(ex)
    finally:
        client.close()
        return res_data

def select_recipe_comment(res):
    try:
        res_data = None  # 定义返回值
        # re = None
        # res_su = None
        # time=None
        client=POOL.connection()#链接池创建链接
        today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # print(today_date)
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql1=sql_mydetails.get("select_user_id").format(telephone=res['telephone'])
        cursor.execute(sql1)
        re=cursor.fetchone()
        # print(re)
        sql2=sql_mydetails.get('insert_comment').format(order_id=res['order_id'],user_id=re['id'],comm=res['content'],comment_time=today_date,scenic_id=res['scenic_id'])
        cursor.execute(sql2)  # 执行sql语句
        res_data = int(cursor.lastrowid)
        # print(res_data)
        sql = sql_mydetails.get('update_order_ticket').format(order_id=res['order_id'],order_start=res['order_start'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_su = int(cursor.lastrowid)#获取返回的数据  只取一条

        # print(res_data)
        # print(res_su)
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
        print(ex)
    finally:
        client.close()
        return res_data
# if __name__ == '__main__':
#     a={"order_id":'201902192001568'}
#     get_order_mydetail(a)