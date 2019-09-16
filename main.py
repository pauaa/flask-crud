import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_password = os.environ['DB_PWD']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:{pwd}@localhost/test'.format(pwd=db_password)

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)


@app.route('/users/')
def users_api():
    users = User.query.all()
    # print(jsonify(users))
    return jsonify([{u.id: u.name} for u in users])


@app.route('/users/<id>')
def user_api(id):
    user = User.query.filter_by(id=id).first()
    print(user)
    return str(user)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
