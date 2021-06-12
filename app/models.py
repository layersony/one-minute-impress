from datetime import datetime
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from datetime import datetime

class User(db.Model):
  __tablename__ = 'user'

  id= db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  profile_pic = db.Column(db.String())
  pass_secure = db.Column(db.String(255))
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  comments = db.relationship('Comment', backref='user', lazy= 'dynamic')
  date_join = db.Column(db.DateTime, default = datetime.utcnow())

  @property
  def password(self):
    raise AttributeError('You Cannot Read the password Attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)

  def __repr__(self):
    return f'User {self.username}'
  
