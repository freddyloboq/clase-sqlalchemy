from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dataBaseUsers.db"
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/get_users', methods=['GET'])
def get_users():
  get_users = User().query.all()
  # [<User 1>, <User 2>, <User 3>, <User 4>, <User 5>, <User 6>, <User 7>]
  get_users_serialize = list(map(lambda user: user.serialize(), get_users))
  print(get_users_serialize)
  return jsonify({"mjs": "success", "data": get_users_serialize})

@app.route('/create', methods=['POST'])
def create_user():
  data = request.get_json()

  user_exist = User.query.filter_by(email=data['email']).first()
  print(user_exist)

  if user_exist is not None:
    return jsonify({"response": "error, try with another email"}), 404
  else:
    create_user = User()
    create_user.name = data['name']
    create_user.email = data['email']
    create_user.password = data['password']

    db.session.add(create_user)
    db.session.commit()
    return jsonify({"response": "create acount", "data": data}), 201

# <valor>
@app.route('/edit_user/<int:id>', methods=['PUT'])
def edit_user(id):
  print(id)
  data = request.get_json()
  find_user = User().query.filter_by(id=id).first()

  if find_user is not None:
    find_user.name = data['name']
    find_user.email = data['email']
    find_user.password = data['password']

    print(find_user)

    db.session.commit()
    return jsonify({"message": "Edit successfully", "data": find_user.serialize()})
  else:
    return jsonify({"message": "not found"})

app.run(host="localhost" ,port=8080 , debug=True)