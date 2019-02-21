from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing Flask Extensions
bootstrap = Bootstrap()

app = Flask(__name__)


# Setting up configuration
app.config.from_object(DevConfig)

# Initializing flask Extensions
bootstrap.init_app(app)

from app import views
