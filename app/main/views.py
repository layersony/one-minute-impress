from . import main
from flask import render_template, abort, url_for, redirect
from ..models import Pitch, User, Comment
from .forms import PitchForm, UpdateForm, CommentForm, VoteForm
from flask_login import login_required, current_user
@main.route('/')
def index():
  pitch = Pitch.query.all()
  vote_form = VoteForm()

  return render_template('index.html', pitch=pitch, vote_form=vote_form)
