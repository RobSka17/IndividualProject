from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import CardStats, Users
from flask_login import current_user
from application import bcrypt

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
	lepidoptera = BooleanField('Lepidoptera')
	noble = BooleanField('Noble')
	staff = BooleanField('Staff')
	warrior = BooleanField('Warrior')
	allclasses = BooleanField('Check all')

	submit = SubmitField('Go')

class SearchByTypeForm(FlaskForm):

	all_types = [('Bug','Bug'),('Business','Business'),('Dark','Dark'),('Earth','Earth'),('Fire','Fire'),('Light','Light'),('Machine','Machine'),('Water','Water')]

	select_type = SelectField('Select Type: ', choices = all_types)

	arachnid = BooleanField('Arachnid')
	beast = BooleanField('Beast')
	boss = BooleanField('Boss')
	demon = BooleanField('Demon')
	fish = BooleanField('Fish')
	flame = BooleanField('Flame')
	food = BooleanField('Food')
	goodboi = BooleanField('Good Boi')
	larva = BooleanField('Larva')
	lepidoptera = BooleanField('Lepidoptera')
	noble = BooleanField('Noble')
	staff = BooleanField('Staff')
	warrior = BooleanField('Warrior')
	allclasses = BooleanField('Check all')

	submit = SubmitField('Go')

class SearchByClassForm(FlaskForm):

	all_classes = [('Arachnid','Arachnid'),('Beast','Beast'),('Boss','Boss'),('Demon','Demon'),('Fish','Fish'),('Flame','Flame'),('Food','Food'),('Good Boi','Good Boi'),('Larva','Larva'),('Lepidoptera','Lepidoptera'),('Noble','Noble'),('Staff','Staff'),('Warrior','Warrior')]

	select_class = SelectField('Select Class: ', choices = all_classes)

	light = BooleanField('Light')
	dark = BooleanField('Dark')
	fire = BooleanField('Fire')
	water = BooleanField('Water')
	machine = BooleanField('Machine')
	bug = BooleanField('Bug')
	business = BooleanField('Business')
	earth = BooleanField('Earth')
	alltypes = BooleanField('Check all')

	submit = SubmitField('Go')


class DeckBuilder(FlaskForm):

	deckname = StringField('Search:',
	validators=[
	Length(min=1, max=100)
	])
	submit2 = SubmitField('Build my deck!')
	decksize = IntegerField('Choose deck size:')
	all_cards = []

	all_cards.append(('none','-- None --'))

	for card in CardStats.query.all():
		all_cards.append((card.name,card.name))

	cardselect1 = SelectField('Card 1', choices = all_cards)
	cardselect2 = SelectField('Card 2', choices = all_cards)
	cardselect3 = SelectField('Card 3', choices = all_cards)
	cardselect4 = SelectField('Card 4', choices = all_cards)
	cardselect5 = SelectField('Card 5', choices = all_cards)
	cardselect6 = SelectField('Card 6', choices = all_cards)
	cardselect7 = SelectField('Card 7', choices = all_cards)
	cardselect8 = SelectField('Card 8', choices = all_cards)
	cardselect9 = SelectField('Card 9', choices = all_cards)
	cardselect10 = SelectField('Card 10', choices = all_cards)
	cardselect11 = SelectField('Card 11', choices = all_cards)
	cardselect12 = SelectField('Card 12', choices = all_cards)
	cardselect13 = SelectField('Card 13', choices = all_cards)
	cardselect14 = SelectField('Card 14', choices = all_cards)
	cardselect15 = SelectField('Card 15', choices = all_cards)
	cardselect16 = SelectField('Card 16', choices = all_cards)
	cardselect17 = SelectField('Card 17', choices = all_cards)
	cardselect18 = SelectField('Card 18', choices = all_cards)
	cardselect19 = SelectField('Card 19', choices = all_cards)
	cardselect20 = SelectField('Card 20', choices = all_cards)
	cardselect21 = SelectField('Card 21', choices = all_cards)
	cardselect22 = SelectField('Card 22', choices = all_cards)
	cardselect23 = SelectField('Card 23', choices = all_cards)
	cardselect24 = SelectField('Card 24', choices = all_cards)
	cardselect25 = SelectField('Card 25', choices = all_cards)
	cardselect26 = SelectField('Card 26', choices = all_cards)
	cardselect27 = SelectField('Card 27', choices = all_cards)
	cardselect28 = SelectField('Card 28', choices = all_cards)
	cardselect29 = SelectField('Card 29', choices = all_cards)
	cardselect30 = SelectField('Card 30', choices = all_cards)

class DeckSelect(FlaskForm):
	decksearch = StringField('Search for your deck: ')
	submit = SubmitField('Modify')
	preview = SubmitField('Preview')
	search_all_check = BooleanField('(Check to skip search and show all decks)')

	deckselect = SelectField('Select a deck: ', choices = [])

	
class DeckModifier(FlaskForm):
	all_cards = []

	all_cards.append(('none','-- None --'))

	for card in CardStats.query.all():
		all_cards.append((card.name,card.name))

	cardselect1 = SelectField('Card 1', choices = all_cards)
	cardselect2 = SelectField('Card 2', choices = all_cards)
	cardselect3 = SelectField('Card 3', choices = all_cards)
	cardselect4 = SelectField('Card 4', choices = all_cards)
	cardselect5 = SelectField('Card 5', choices = all_cards)
	cardselect6 = SelectField('Card 6', choices = all_cards)
	cardselect7 = SelectField('Card 7', choices = all_cards)
	cardselect8 = SelectField('Card 8', choices = all_cards)
	cardselect9 = SelectField('Card 9', choices = all_cards)
	cardselect10 = SelectField('Card 10', choices = all_cards)
	cardselect11 = SelectField('Card 11', choices = all_cards)
	cardselect12 = SelectField('Card 12', choices = all_cards)
	cardselect13 = SelectField('Card 13', choices = all_cards)
	cardselect14 = SelectField('Card 14', choices = all_cards)
	cardselect15 = SelectField('Card 15', choices = all_cards)
	cardselect16 = SelectField('Card 16', choices = all_cards)
	cardselect17 = SelectField('Card 17', choices = all_cards)
	cardselect18 = SelectField('Card 18', choices = all_cards)
	cardselect19 = SelectField('Card 19', choices = all_cards)
	cardselect20 = SelectField('Card 20', choices = all_cards)
	cardselect21 = SelectField('Card 21', choices = all_cards)
	cardselect22 = SelectField('Card 22', choices = all_cards)
	cardselect23 = SelectField('Card 23', choices = all_cards)
	cardselect24 = SelectField('Card 24', choices = all_cards)
	cardselect25 = SelectField('Card 25', choices = all_cards)
	cardselect26 = SelectField('Card 26', choices = all_cards)
	cardselect27 = SelectField('Card 27', choices = all_cards)
	cardselect28 = SelectField('Card 28', choices = all_cards)
	cardselect29 = SelectField('Card 29', choices = all_cards)
	cardselect30 = SelectField('Card 30', choices = all_cards)

	submitdeck = SubmitField('Save Changes')
	deletedeck = SubmitField('Delete Deck')

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
		DataRequired(),
		Length(min=2, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
		DataRequired(),
		Length(min=2, max=30)
		])
	email = StringField('Email',
		validators=[
		DataRequired(),
		Email()
		])
	password = PasswordField('Password',
		validators=[
		DataRequired(),
		Length(min=6)
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
		DataRequired(),
		EqualTo('password')
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
			])
	password = PasswordField('Password',
		validators=[
			DataRequired(),
			])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log in')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if not user:
			raise ValidationError('No account exists under the given user ID. Check your details and try again.')

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
		DataRequired(),
		Length(min=2, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
		DataRequired(),
		Length(min=2, max=30)
		])
	email = StringField('Email',
		validators=[
		DataRequired(),
		Email()
		])
	submit = SubmitField('Update')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use!')

class DeleteAccountForm(FlaskForm):
	password = PasswordField('Enter Password:',
		validators=[
		DataRequired()])
	delete = SubmitField('Delete Account')