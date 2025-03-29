from flask import Flask
def create_app():
    app= Flask(__name__)
    app.config['DATABASE']='schma.sql'
    app.config['SECRET_KEY']= 'secret'

    from . import main
    app.register_blueprint(main.bp)

    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)

    return app
