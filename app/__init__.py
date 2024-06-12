from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler

db = SQLAlchemy()
migrate = Migrate()
scheduler = APScheduler()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    scheduler.init_app(app)
    scheduler.start()

    from app import routes
    app.register_blueprint(routes.bp)

    return app
