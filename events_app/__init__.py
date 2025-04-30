from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from events_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

from events_app.routes import main

app.register_blueprint(main)

with app.app_context():

    from events_app.models import Event, Guest, guest_event_table

    db.drop_all()
    db.create_all()
