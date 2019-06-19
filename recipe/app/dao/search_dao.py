from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_search import sql_user

def search1(id):
    try:
        client = POOL.connection()
        res_search1=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('search1').format(tid=id['tid'])
        cursor.execute(sql)
        res_search1= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_search1

def search2(id):
    try:
        client = POOL.connection()
        res_search2=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('search2').format(tname=id['tname'])
        cursor.execute(sql)
        res_search2= cursor.fetchall()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_search2


def search3(id):
    try:
        client = POOL.connection()
        res_search3=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('search3').format(tname=id['tname'])
        cursor.execute(sql)
        res_search3= cursor.fetchall()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_search3


# if __name__ == '__main__':
#     s={'tname':'苏州'}
#     print(search3(s))



