from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class CardStats(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	path=db.Column(db.String(250), nullable=True, unique=True)
	name = db.Column(db.String(250), nullable=False, unique=True)
	type = db.Column(db.String(50), nullable=False)
	class1=db.Column(db.String(100), nullable=False)
	class2=db.Column(db.String(100), nullable=True)
	attack=db.Column(db.Integer, nullable=False)
	defence=db.Column(db.Integer, nullable=False)
	alignment=db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return ''.join(['ID: ', str(self.id), '\r\n',
			'Name: ', self.name, '\r\n',
			'Type: ', self.type, '\r\n',
			'Class 1: ', self.class1, '\r\n',
			'Class 2: ', self.class2, '\r\n',
			'Attack: ', str(self.attack), '\r\n',
			'Defence: ', str(self.defence), '\r\n',
			'Alignment : ', str(self.alignment)])

class Decks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False, unique=True)
	cards = db.Column(db.String, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join(['ID: ', str(self.id), '\r\n',
			'Name: ', self.name, '\r\n',
			'Cards', self.cards])



class Users(db.Model, UserMixin):
	
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(50), nullable = False)
	decks = db.relationship('Decks', backref='author', lazy=True)


	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n',
			'Email: ', self.email, '\r\n',
			'Name: ', self.first_name, ' ', self.last_name])
