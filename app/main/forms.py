from flask_wtf import FlaskForm, Form # will help us create form
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  title = StringField('Pitch Title', validators=[Required()])
  content = TextAreaField('Pitch Content', validators=[Required()])
  category = SelectField('Category', choices=[('-----','-----'),('PickUp Lines','PickUp Lines'), ('Inspirational','Inspirational'), ('Product Slogan', 'Product Slogan')])
  submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
  bio = TextAreaField('Text us about you', validators=[Required()])
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  comment = TextAreaField('')
  submit = SubmitField('Submit')

class VoteForm(Form):
  vote = RadioField('Vote', choices=[('upvote', 'UpVote'), ('downvote', 'DownVote')])
  submit = SubmitField('Submit Vote')