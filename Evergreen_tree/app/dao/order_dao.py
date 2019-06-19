from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_order import sql_order

def get_ticket(res):
    try:
        res1 = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_order.get('get_ticket').format(tid=res["tid"])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res1 = cursor.fetchall()

        client.commit()

    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res1


def order_create(res):
    try:

        from datetime import datetime
        now = datetime.now()
        strnow = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        res1 = None
        res2=None
        user_id=None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql1=sql_order.get('getUserById').format(telephone=res["telephone"])
        cursor.execute(sql1)
        res2=cursor.fetchone()
        user_id=res2['id']
        sql = sql_order.get('order_create').format(order_id=res["order_id"], scenic_id=res["scenic_id"],
                                                   user_id=user_id,order_time=strnow, tourst_time=res["tourst_time"], onum=res["onum"],
                                                   oname=res["oname"], otelephone=res["otelephone"],
                                                   order_start=res["order_start"])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res1 = int(cursor.lastrowid)
        # print(res1)
        client.commit()

    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res1
def get_info(res):
    try:
        res3={}
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_order.get('getOrderinfo').format(order_id=res["order_id"])
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res1 = cursor.fetchone()
        sql1=sql_order.get('get_ticket').format(tid=res1['scenic_id'])
        cursor.execute(sql1)
        res2=cursor.fetchone()
        # print(res1)
        # print(res2)
        client.commit()
        res3.update(res1)
        res3.update(res2)
        # print(res3)
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res3

def update_order(res):
    try:
        res1 = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = sql_order.get('update_ticket').format(order_id=res["order_id"],order_start=res["order_start"])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res1 = int(cursor.lastrowid)

        client.commit()

    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res1
def select_order(res):
    try:
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        res1 = None
        # 4. 准备sql语句
        sql = sql_order.get('select_ticket').format(order_id=res["order_id"])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res1 = cursor.fetchone()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res1
# if __name__ == '__main__':
#     # user = {
#     #     "order_id": "201902161512720", "scenic_id": 1,
#     #     "tourst_time": "2019-2-16", "onum": 4, "oname":"唐扬", "otelephone": "18792031925", "order_start": 1,
#     #     "telephone":"18792031925"
#     # }
#     user={
#         "order_id":"201902161706756",
#     }
#     # print(user)
#     get_info(user)
# if __name__ == '__main__':
#     user={
#         "order_id":"201902201702110"
#     }
#     select_order(user)