from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  email = db.Column(db.String(40), nullable=False)
  password = db.Column(db.String(50), nullable=False)

  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email
    }