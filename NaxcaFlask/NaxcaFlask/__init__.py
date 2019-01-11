from flask import Flask
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore
from NaxcaFlask.database import db_session, init_db
from NaxcaFlask.models import User, Role


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    init_db()
    user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
    app.security = Security(app, user_datastore)


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    #from NaxcaFlask.users import users_blueprint
    #app.register_blueprint(users_blueprint)
    pass