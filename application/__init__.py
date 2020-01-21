from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# REMINDER: For the purposes of this application, this key is safe to include in source code.
# For any projects handling sensitive information, export such keys in environment variables instead.
app.config['SECRET_KEY'] = '4K6eQpi7n2bxDau'



from application import routes
