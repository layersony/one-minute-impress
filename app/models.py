from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from flask_login import UserMixin, current_user

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
  likes = db.relationship('Likes', backref = 'pitch', lazy = 'dynamic')
  dislikes = db.relationship('Dislikes', backref = 'pitch', lazy = 'dynamic')
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

class Likes(db.Model):
  __tablename__ = 'likes'

  id = db.Column(db.Integer,primary_key=True)
  likes = db.Column(db.Integer,default=1)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

  def save_likes(self):
      db.session.add(self)
      db.session.commit()

  @classmethod
  def add_likes(cls,id):
      likes_pitch = cls(user = current_user, pitch_id=id)
      likes_pitch.save_likes()

  
  @classmethod
  def get_likes(cls,id):
      likes = cls.query.filter_by(pitch_id=id).all()
      return likes

  @classmethod
  def get_all_likes(cls):
      likes = cls.query.order_by('id').all()
      return likes

  def __repr__(self):
      return f'{self.user_id}:{self.pitch_id}'


class Dislikes(db.Model):
  __tablename__ = 'dislikes'

  id = db.Column(db.Integer,primary_key=True)
  dislikes = db.Column(db.Integer,default=1)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

  def save_dislikes(self):
      db.session.add(self)
      db.session.commit()

  @classmethod
  def add_dislikes(cls,id):
      dislikes_pitch = cls(user = current_user, pitch_id=id)
      dislikes_pitch.save_dislikes()

  
  @classmethod
  def get_dislikes(cls,id):
      dislikes = cls.query.filter_by(pitch_id=id).all()
      return dislikes

  @classmethod
  def get_all_dislikes(cls):
      dislikes = cls.query.order_by('id').all()
      return dislikes

  def __repr__(self):
      return f'{self.user_id}:{self.pitch_id}'

      
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
