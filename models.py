from main import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(256), nullable=False)

class Choice(db.Model):
    __tablename__ = 'choices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    choice = db.Column(db.String(256), nullable=False)

    question = db.relationship('Question', backref=db.backref('choices'))

class Answer(db.Model):
    __tablename__ = 'answers'
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('choices.id'), nullable=False)
