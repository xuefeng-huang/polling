from flask import Blueprint
from .models import Question, Choice, Answer, User
from shared import db
from flask import request, jsonify, make_response


polling = Blueprint('polling', __name__)

@polling.route('/questions', methods=['POST'])
def create_question():
    question_text = request.get_json()['question']
    q = Question(question=question_text)
    db.session.add(q)
    db.session.commit()

    data = {'message': 'Created'}
    return make_response(jsonify(data), 201)

@polling.route('/choice', methods=['POST'])
def create_choice():
    question_id = request.get_json()['question_id']
    text = request.get_json()['text']

    c = Choice(question_id=question_id, choice=text)
    db.session.add(c)
    db.session.commit()

    data = {'message': 'Created'}
    return make_response(jsonify(data), 201)

@polling.route('/answer', methods=['POST'])
def save_answer():
    user_id = request.get_json()['user_id']
    question_id = request.get_json()['question_id']
    answer_id = request.get_json()['answer_id']

    a = Answer(user_id=user_id, question_id=question_id, answer_id=answer_id)
    db.session.add(a)
    db.session.commit()

    data = {'message': 'Created'}
    return make_response(jsonify(data), 201)

@polling.route('/user', methods=['POST'])
def create_user():
    user_name = request.get_json()['user_name']
    u = User(username=user_name)

    db.session.add(u)
    db.session.commit()

    data = {'message': 'Created'}
    return make_response(jsonify(data), 201)