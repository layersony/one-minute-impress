from . import main
from .. import db, photos
from flask import render_template, abort, url_for, redirect, request
from ..models import Pitch, User, Comment, Likes, Dislikes
from .forms import PitchForm, UpdateForm, CommentForm
from flask_login import login_required, current_user


@main.route('/')
def index():
  pickup = Pitch.get_pitch_category('PickUp Lines')
  slogan = Pitch.get_pitch_category('Product Slogan')
  inspire = Pitch.get_pitch_category('Inspirational')

  return render_template('index.html', pickup=pickup, inspire=inspire, slogan=slogan)

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

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic = path
    db.session.commit()
  return redirect(url_for('main.profile', uname=uname))

@main.route('/newpitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
  pitchform = PitchForm()

  if pitchform.validate_on_submit():
    title = pitchform.title.data
    content = pitchform.content.data
    category = pitchform.category.data

    new_pitch = Pitch(title=title, content=content, category=category, user_id=current_user.id)
    print(new_pitch)
    new_pitch.save_pitch()
    return redirect(url_for('main.profile', uname=current_user.username))

  
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
  
  pitchComment = Comment.query.filter_by(pitch_id=id).all()
  print(pitchComment)
  return render_template('profile/comment.html', comment=form,pitch=pitch, pitchcomment = pitchComment)

@main.route('/pitch/likes/<pitch_id>', methods = ['GET', 'POST'])
@login_required
def likes(pitch_id):    
    if Likes.query.filter(Likes.user_id==current_user.id,Likes.pitch_id==pitch_id).first():
        return redirect(url_for('main.index'))

    new_likes = Likes(pitch_id=pitch_id, user_id = current_user.id)
    new_likes.save_likes()
    return redirect(url_for('main.index'))

@main.route('/pitch/dislikes/<pitch_id>', methods = ['GET', 'POST'])
@login_required
def dislikes(pitch_id):
    if Dislikes.query.filter(Dislikes.user_id==current_user.id,Dislikes.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))

    new_dislikes = Dislikes(pitch_id=pitch_id, user_id = current_user.id)
    new_dislikes.save_dislikes()
    return redirect(url_for('main.index'))
