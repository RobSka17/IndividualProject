from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from application.models import CardStats

class SearchByNameForm(FlaskForm):
	search_term = StringField('Search:',
	validators=[
	Length(min=0, max=100)
	])
	light = BooleanField('Light')
	dark = BooleanField('Dark')
	fire = BooleanField('Fire')
	water = BooleanField('Water')
	machine = BooleanField('Machine')
	bug = BooleanField('Bug')
	business = BooleanField('Business')
	earth = BooleanField('Earth')

	arachnid = BooleanField('Arachnid')
	beast = BooleanField('Beast')
	boss = BooleanField('Boss')
	demon = BooleanField('Demon')
	fish = BooleanField('Fish')
	food = BooleanField('Food')
	goodboi = BooleanField('Good Boi')
	larva = BooleanField('Larva')
	noble = BooleanField('Noble')
	staff = BooleanField('Staff')
	warrior = BooleanField('Warrior')

	submit = SubmitField('Go')