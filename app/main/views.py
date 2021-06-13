from . import main
from .. import db
from flask import render_template, abort, url_for, redirect
from ..models import Pitch, User, Comment
from .forms import PitchForm, UpdateForm, CommentForm, VoteForm
from flask_login import login_required, current_user


@main.route('/')
def index():
  pitch = Pitch.query.all()
  vote_form = VoteForm()
  

  return render_template('index.html', pitch=pitch, vote_form=vote_form)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  
  if user is None:
    abort(404)
  else:
    pitches = Pitch.query.filter_by(user_id=current_user.id).all()
    return render_template('profile/profile.html', user = user, pitches = pitches)

@main.route('/update/<uname>/profile', methods = ['GET', 'POST'])
@login_required
def update(uname):
  form = UpdateForm()
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)
  
  if form.validate_on_submit():
    user.bio = form.bio.data
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('.profile', uname=user.username ))

  return render_template('profile/update.html', form=form)

@main.route('/newpitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
  pitchform = PitchForm()

  if pitchform.validate_on_submit():
    title = pitchform.title.data
    content = pitchform.content.data
    category = pitchform.category.data

    new_pitch = Pitch(title=title, content=content, category=category, user_id=current_user.id,likes=0, dislikes=0)
    print(current_user)
    new_pitch.save_pitch()
    return redirect(url_for('main.index'))

  
  return render_template('newpitch.html', pitchform = pitchform)

@main.route('/comment/<id>', methods=['GET', 'POST'])
@login_required
def comment(id):
  form = CommentForm()
  pitch = Pitch.query.filter_by(id=id).first()

  if form.validate_on_submit():
    comment = form.comment.data
    
    new_comment = Comment(comment = comment, user_id = current_user.id, pitch_id = id)

    new_comment.save_comment()
    return redirect(url_for('main.index'))
  
  return render_template('profile/comment.html', comment=form,pitch=pitch)

