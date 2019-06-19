from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_index import sql_user



def rande(id):
    try:
        client = POOL.connection()
        res_pic1=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('rande').format()
        cursor.execute(sql)
        res_pic1= cursor.fetchall()
        client.commit()
        print(res_pic1)
    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic1
if __name__ == '__main__':
    rande(id)



# index 开始
def getpic1(id):
    try:
        client = POOL.connection()
        res_pic1=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic1').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic1= cursor.fetchone()
        client.commit()
        print(res_pic1)
    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic1

def getpic2(id):
    try:
        client = POOL.connection()
        res_pic2=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic2').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic2= cursor.fetchone()
        client.commit()
        print(res_pic2)
    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic2

def getpic3(id):
    try:
        client = POOL.connection()
        res_pic3=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic3').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic3= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic3

def getpic4(id):
    try:
        client = POOL.connection()
        res_pic4=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic4').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic4= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic4


def getpic5(id):
    try:
        client = POOL.connection()
        res_pic5=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic5').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic5= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic5

def getpic6(id):
    try:
        client = POOL.connection()
        res_pic6=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic6').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic6= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic6

def getpic7(id):
    try:
        client = POOL.connection()
        res_pic7=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic7').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic7= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic7

def getpic8(id):
    try:
        client = POOL.connection()
        res_pic8=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic8').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic8= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic8

def getpic9(id):
    try:
        client = POOL.connection()
        res_pic9=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic9').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic9= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic9

def getpic10(id):
    try:
        client = POOL.connection()
        res_pic10=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getpic10').format(tid=id['tid'])
        cursor.execute(sql)
        res_pic10= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_pic10


def getwords1(id):
    try:
        client = POOL.connection()
        res_words1=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getwords1').format(tid=id['tid'])
        cursor.execute(sql)
        res_words1= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_words1


def getwords2(id):
    try:
        client = POOL.connection()
        res_words2=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getwords2').format(tid=id['tid'])
        cursor.execute(sql)
        res_words2= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_words2

def getwords3(id):
    try:
        client = POOL.connection()
        res_words3=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('getwords3').format(tid=id['tid'])
        cursor.execute(sql)
        res_words3= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return res_words3

def get1(id):
    try:
        client = POOL.connection()
        tj1=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('get1').format(tid=id['tid'])
        cursor.execute(sql)
        tj1= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return tj1


def get2(id):
    try:
        client = POOL.connection()
        tj2=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('get2').format(tid=id['tid'])
        cursor.execute(sql)
        tj2= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return tj2

def get3(id):
    try:
        client = POOL.connection()
        tj3=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sql_user.get('get3').format(tid=id['tid'])
        cursor.execute(sql)
        tj3= cursor.fetchone()
        client.commit()

    except Exception as ex:
        client.rollbake()
    finally:
        client.close()
        return tj3



