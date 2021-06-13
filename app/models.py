from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
  __tablename__ = 'users'

  id= db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  profile_pic = db.Column(db.String())
  pass_secure = db.Column(db.String(255))
  comments = db.relationship('Comment', backref='users', lazy= 'dynamic')
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

class Pitch(db.Model):
  __tablename__ = 'pitch'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  content = db.Column(db.String())
  category = db.Column(db.String())
  posted = db.Column(db.DateTime, default=datetime.utcnow())
  likes = db.Column(db.Integer)
  dislikes = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  comments = db.relationship('Comment', backref='pitch', lazy='dynamic')

  def save_pitch(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitch_category(cls, group):
    return cls.query.filter_by(category=group).all()
    
class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key = True)
  comment = db.Column(db.String(2000))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def get_specific_comment(cls, id):
    return cls.query.filter_by(pitch_id = id).all()


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))