from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class LoginForm(FlaskForm):
  email = StringField('Your Email Address', validators=[Required(), Email()])
  password = PasswordField('Password', validators=[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Sign In')

class Registration(FlaskForm):
  email = StringField('Your Email Address', validators=[Required(), Email()])
  username = StringField('username', validators=[Required()])
  password = PasswordField('Password', validators=[Required(), EqualTo('pass_confirm', message = 'Passwords Must Match')])
  pass_confirm = PasswordField('Confirm Password', validators = [Required()])
  submit =  SubmitField()

  def validate_email(self, data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError('There is an Account with that Email')
    
  def validate_username(self, data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError('That Username is taken')