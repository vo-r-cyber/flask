from flask import Blueprint, render_template, g

bp=Blueprint('main',__name__)

@bp.route('/')
def index():
    user=g.user
    return render_template('index.html',user=user)
