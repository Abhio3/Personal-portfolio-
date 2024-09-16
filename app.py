from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))  # current location of my folder

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')  # Creating database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True  # This is modification Tracker by SQL Alchemy

db = SQLAlchemy(app)  # passing object to create database
ma = Marshmallow(app)  # passing object for serialization to create schema

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    ta = db.Column(db.String(500))


    def __init__(self, name, email, ta):
        self.name = name
        self.email = email
        self.ta = ta

# User schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'ta')

user_schema = UserSchema()


@app.route('/',methods=["POST","GET"])
def index ():
    
    if request.method == "POST":
        name = request.form['Name']
        email = request.form['Email']
        ta = request.form['ta']
    
        new_user = User(name,email,ta)
    
        db.session.add(new_user)
        db.session.commit()
    
    
    return render_template("index.html")



if __name__ == "__main__":
        app.run(debug=True, port=4000)

    