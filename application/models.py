from application import db

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