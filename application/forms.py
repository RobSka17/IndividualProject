from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
from application.models import CardStats

class SearchByNameForm(FlaskForm):
	search_term = StringField('Search:',
	validators=[
	Length(min=1, max=100)
	])
	light = BooleanField('Light')
	dark = BooleanField('Dark')
	fire = BooleanField('Fire')
	water = BooleanField('Water')
	machine = BooleanField('Machine')
	bug = BooleanField('Bug')
	business = BooleanField('Business')
	earth = BooleanField('Earth')
	alltypes = BooleanField('Check all')

	arachnid = BooleanField('Arachnid')
	beast = BooleanField('Beast')
	boss = BooleanField('Boss')
	demon = BooleanField('Demon')
	fish = BooleanField('Fish')
	flame = BooleanField('Flame')
	food = BooleanField('Food')
	goodboi = BooleanField('Good Boi')
	larva = BooleanField('Larva')
	noble = BooleanField('Noble')
	staff = BooleanField('Staff')
	warrior = BooleanField('Warrior')
	allclasses = BooleanField('Check all')

	submit = SubmitField('Go')

class DeckBuilder(FlaskForm):

	deckname = StringField('Deck Name:')
	submit2 = SubmitField('Build my deck!')

	cardselect = SelectField[('1','K-Knight'),('2','Fish Lord')]
