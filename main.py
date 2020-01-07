from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from views import *
from models import User, Question, Choice, Answer

if __name__ == '__main__':
    # recreate tables and insert 2 default users
    db.drop_all()
    db.create_all()
    db.session.commit()

    u1 = User(username='joe')
    u2 = User(username='mark')
    db.session.add_all([u1, u2])
    db.session.commit()

    app.run()