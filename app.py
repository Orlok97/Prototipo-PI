from flask import Flask
from controllers import *
from models import db

app = Flask(__name__,template_folder='views')
app.secret_key='123456789'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/flask_proto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
with app.app_context():
    db.create_all()
 
@app.route('/',methods=['GET','POST'])
def index():
    return LoginController().index()

@app.route('/cadastro',methods=['GET','POST'])
def cadastro():
    return CadastroController().index()

@app.route('/home',methods=['GET','POST'])
def home():
    return HomeController().index()
@app.route('/logout')   
def logout():
    return HomeController().logout()


if __name__ == '__main__':
    app.run(debug=True)