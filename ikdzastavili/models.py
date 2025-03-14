#from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin
#app = Flask (__name__)

#app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db' 
#db = SQLAlchemy(app)
db = SQLAlchemy

class UserAccount(db.Model, UserMixin):
    __tablename__ = 'user_account'
    user_account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registration_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), unique=True, nullable=False)
    category_description = db.Column(db.String(255))
#with app.app_context():
    #db.create_all()
    #db.session.commit()