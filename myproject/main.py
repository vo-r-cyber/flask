from flask import Blueprint, render_template, g
from .auth import login_required

bp=Blueprint('main',__name__)

@bp.route('/')
@login_required
def index():
    user=g.user
    return render_template('index.html',user=user)
