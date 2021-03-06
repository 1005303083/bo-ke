import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from back.models import db
from back.views import back_blueprint
from web.views import  web_blueprint

app = Flask(__name__)

app.register_blueprint(blueprint=back_blueprint, url_prefix='/back')
app.register_blueprint(blueprint=web_blueprint, url_prefix='/web')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/work01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SESSION_TYPE']='redis'
app.config['SESSION_REDIS']=redis.Redis(host='127.0.0.1',port=6379)

app.secret_key='rgaerthyiyjdi6jgrthwsg45ykj8kusu78ks'
Session(app)
db.init_app(app)

if __name__ == '__main__':
    manage = Manager(app)
    manage.run()



