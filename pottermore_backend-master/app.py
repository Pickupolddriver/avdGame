from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from models.user import User
from flask_login import LoginManager, login_user, logout_user , current_user , login_required
import json
from bson import json_util

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'mansiboriya'
login_manager = LoginManager()
login_manager.init_app(app)

client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.adventure_quest #Select the database
users = db.users #Select the collection name

@app.route('/')
def demo():
  return "Hello World"


# Authentication Block

@app.route("/login", methods=['POST'])
def login():
  req = request.get_json(silent=True)
  id = req.get('user_id')
  user1 = User.get(users, id)
  login_user(user1)
  return json_util.dumps(user1.__dict__, default=lambda o: o.__dict__)

@app.route("/login/password", methods=['POST'])
def login_password():
  req = request.get_json(silent=True)
  password = req.get('password')
  user1 = User.get_by_password(users, password)
  if user1 is not None:
      login_user(user1)
  return json_util.dumps(current_user.__dict__, default=lambda o: o.__dict__)

@app.route("/logout", methods=['POST'])
def logout():
  logout_user()
  return {'status': True}

@login_manager.header_loader
def load_user_from_header(header_val):
    header_val = header_val.replace('Basic ', '', 1)
    u = User.get_by_password(users, header_val)
    return u

if __name__ == "__main__":
  app.run()

