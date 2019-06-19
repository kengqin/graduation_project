from app.app import app
from app.route_user import user
from app.route_order import orders
from app.route_detail import detail
from app.route_myorder import myorder
from app.route_mydetails import my_details
from app.route_personaldate import personalDate
from app.route_collection import my_collection
from app.route_comment import comment
from app.route_purchaser import purchaser
from app.route_safety import safety
from app.route_index import index
from app.route_search import search
from app.route_sceipe import sceipe

# 构建蓝图
app.register_blueprint(index, url_prefix='/api/index')
app.register_blueprint(user, url_prefix='/api/user')
app.register_blueprint(orders, url_prefix='/api/orders')
app.register_blueprint(detail, url_prefix='/api/detail')
app.register_blueprint(myorder, url_prefix='/api/myorder')
app.register_blueprint(my_details, url_prefix='/api/my_details')
app.register_blueprint(personalDate, url_prefix='/api/personalDate')
app.register_blueprint(my_collection, url_prefix='/api/my_collection')
app.register_blueprint(comment, url_prefix='/api/comment')
app.register_blueprint(purchaser, url_prefix='/api/purchaser')
app.register_blueprint(safety, url_prefix='/api/safety')
app.register_blueprint(search, url_prefix='/api/search')
app.register_blueprint(sceipe, url_prefix='/api/sceipe')




@app.route('/api/v1')
def index():
    return 'INDEX'


@app.errorhandler(404)
def miss(e):
    return '该页面不存在', 404


@app.errorhandler(500)
def error(e):
    return '服务器正在维护...', 500
