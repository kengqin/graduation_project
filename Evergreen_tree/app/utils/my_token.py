import jwt
from app.config import SECRECT_KEY
from functools import wraps
import json
def createToken(tel):
    import datetime
    import hashlib
    # 当前时间加上180秒，意味着token过期时间为12个小时以后
    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60*24*30)
    option = {
        'iss': 'jobapp.com',  # token的签发者
        'exp': datetimeInt,  # 过期时间
        'iat': datetime.datetime.utcnow(),
        'aud': 'webkit',  # token的接收者，这里指定为浏览器
        'telephone': tel  # 放入用户信息，唯一标识，解析后可以使用该消息
    }
    # encoded2 = jwt.encode(payload=option,key= SECRECT_KEY, algorithm='HS256',options= {'verify_exp':True})
    # 这时token类型为字节类型，如果传个前端要进行token.decode()
    token = jwt.encode(option, SECRECT_KEY, 'HS256')
    # print(token)
    return token.decode()
def checkToken(token):
    try:
        decoded = jwt.decode(token, SECRECT_KEY, audience='webkit', algorithms=['HS256'])
        return decoded['telephone']
    except jwt.ExpiredSignatureError as ex:
        return None


def checkLogin(request):
    def decorated(func):
        @wraps(func)
        def wrapper():
            try:
                token = request.headers.get('token')
                print(token)
                decoded = jwt.decode(token, SECRECT_KEY, audience='webkit', algorithms=['HS256'])
                # print(token)
                return func()
            except jwt.ExpiredSignatureError as ex:
                return json.dumps({"status_code": "10007", "status_text": "未登录...."})
        return wrapper
    return decorated