from shared import app, db

from polling_app.views import polling as p
app.register_blueprint(p)
# from views import *
from polling_app.models import User, Question, Choice, Answer

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