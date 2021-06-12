from flask_wtf import FlaskForm # will help us create form
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  title = StringField('Pitch title', validators=[Required()])
  content = TextAreaField('Pitch content', validators=[Required()])
  category = SelectField('Type', choices=[('pickuplines','PickUp Lines'), ('inspirations','Inspirations'), ('slogan', 'Slogan')])
  submit = SubmitField('Submit')
