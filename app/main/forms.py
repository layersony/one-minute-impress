from flask_wtf import FlaskForm, Form # will help us create form
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  title = StringField('Pitch title', validators=[Required()])
  content = TextAreaField('Pitch content', validators=[Required()])
  category = SelectField('Type', choices=[('-----','-----'),('pickuplines','PickUp Lines'), ('inspirations','Inspirations'), ('slogan', 'Slogan')])
  submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
  bio = TextAreaField('Text us about you', validators=[Required()])
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  comment = TextAreaField('Speak out Your Mind')
  submit = SubmitField('Submit')

class VoteForm(Form):
  vote = RadioField('Vote', choices=[('upvote', 'UpVote'), ('downvote', 'DownVote')])
  submit = SubmitField('Submit Vote')