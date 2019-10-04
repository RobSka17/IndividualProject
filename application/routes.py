from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import CardStats, Decks, Users
from application.forms import SearchByNameForm, SearchByTypeForm, SearchByClassForm, DeckBuilder, DeckSelect, DeckModifier, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required

deck_data = []
selected_deck = ""

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/search_by_name', methods=['GET', 'POST'])
def byname():
	srchbyname = SearchByNameForm()
	cardstats = CardStats()

	if srchbyname.validate_on_submit():
		unrefinedcards = cardstats.query.all()
		cards = []
		typefilters = []
		classfilters = []
		for card in unrefinedcards:
			if srchbyname.search_term.data.lower() in card.name.lower():
				if srchbyname.alltypes.data == False:
					for field in srchbyname:
						if field.type == "BooleanField":
							if field.data == True:
								if field.label.text == "Light" or field.label.text == "Dark" or field.label.text == "Fire" or field.label.text == "Water" or field.label.text == "Machine" or field.label.text == "Bug" or field.label.text == "Business" or field.label.text == "Earth":
									typefilters.append(field)
									if field.label.text.lower() == card.type.lower():
										if card not in cards:
											cards.append(card)
				elif srchbyname.allclasses.data == False:
					for field in srchbyname:
						if field.type == "BooleanField":
							if field.data == True:
								if field.label.text == "Arachnid" or field.label.text == "Beast" or field.label.text == "Boss" or field.label.text == "Demon" or field.label.text == "Fish" or field.label.text == "Flame" or field.label.text == "Food" or field.label.text == "Good Boi" or field.label.text == "Larva" or field.label.text == "Noble" or field.label.text == "Staff" or field.label.text == "Warrior": 
									classfilters.append(field)
									if field.label.text.lower() == card.class1.lower() or field.label.text.lower() == card.class2.lower():
										if card not in cards:
											cards.append(card)
				else:
					cards.append(card)


		cards_length = len(cards)

		return render_template('byname.html', title='Search by name', form=srchbyname, cards=cards, cardslength=cards_length)
	else:
		return render_template('byname.html', title='Search by name', form=srchbyname)

@app.route('/search_by_type', methods=['GET', 'POST'])
def bytype():
	srchbytype = SearchByTypeForm()
	cardstats = CardStats()
	if srchbytype.validate_on_submit():
		unrefinedcards = cardstats.query.all()
		cards = []
		classfilters = []
		for card in unrefinedcards:
				if srchbytype.allclasses.data == False:
					for field in srchbytype:
						if field.type == "BooleanField":
							if field.data == True:
								if field.label.text == "Arachnid" or field.label.text == "Beast" or field.label.text == "Boss" or field.label.text == "Demon" or field.label.text == "Fish" or field.label.text == "Flame" or field.label.text == "Food" or field.label.text == "Good Boi" or field.label.text == "Larva" or field.label.text == "Noble" or field.label.text == "Staff" or field.label.text == "Warrior": 
									classfilters.append(field)
									if field.label.text.lower() == card.class1.lower() or field.label.text.lower() == card.class2.lower():
										if card not in cards:
											if card.type == srchbytype.select_type.data:
												cards.append(card)
				else:
					if card.type == srchbytype.select_type.data:
						cards.append(card)

		return render_template('bytype.html', title='Search by type', form=srchbytype, cards=cards)
	else:
		return render_template('bytype.html', title='Search by type', form=srchbytype)

@app.route('/search_by_class', methods=['GET', 'POST'])
def byclass():
	srchbyclass = SearchByClassForm()
	cardstats = CardStats()
	if srchbyclass.validate_on_submit():
		unrefinedcards = cardstats.query.all()
		cards = []
		typefilters = []
		for card in unrefinedcards:
				if srchbyname.alltypes.data == False:
					for field in srchbyname:
						if field.type == "BooleanField":
							if field.data == True:
								if field.label.text == "Light" or field.label.text == "Dark" or field.label.text == "Fire" or field.label.text == "Water" or field.label.text == "Machine" or field.label.text == "Bug" or field.label.text == "Business" or field.label.text == "Earth":
									typefilters.append(field)
									if field.label.text.lower() == card.type.lower():
										if card not in cards:
											if card.class1 == srchbyclass.class_select.data or card.class2 == srchbyclass.class_select.data:
												cards.append(card)
				else:
					if card.type == srchbytype.select_type.data:
						cards.append(card)

		return render_template('byclass.html', title='Search by class', form=srchbyclass, cards=cards)
	else:
		return render_template('byclass.html', title='Search by class', form=srchbyclass)

@app.route('/build_a_deck', methods=['GET', 'POST'])
def builddeck():
	deckbldr = DeckBuilder()
	cardnumber = []
	if deckbldr.decksize.data:
		i = 0
		while i < deckbldr.decksize.data:
			i+=1
			cardnumber.append(i)

	if deckbldr.validate_on_submit():
		print("Submitted")
		deck=[]
		for field in deckbldr:
			if field.type == "SelectField":
				deck.append(field.data)
		newdeck = Decks(name = deckbldr.deckname.data, cards=str(deck), author=current_user)
		db.session.add(newdeck)
		db.session.commit()

		yourdeck = list(eval(newdeck.cards))

		return render_template('builddeck.html', title='Search by name', form=deckbldr, cardnumber=cardnumber, yourdeck=yourdeck)
	else:
		return render_template('builddeck.html', title='Search by name', form=deckbldr, cardnumber=cardnumber)

@app.route('/select_a_deck', methods=['GET', 'POST'])
def selectdeck():
	deckslct = DeckSelect()
	
	global deck_data
	global selected_deck

	deckchoices = []

	for deck in Decks.query.all():
		if deck.user_id == current_user.id:
			deckchoices.append((deck.name, deck.name))

	for field in deckslct:
		if field.type == "SelectField":
			field.choices = deckchoices

	if deckslct.is_submitted():
		selected_deck = deckslct.deckselect.data
		return redirect(url_for('modifydeck'))
	else:
		return render_template('selectdeck.html', title='Existing Decks', form=deckslct, deckdata=deck_data, selectdeck=selected_deck)

@app.route('/modify_a_deck', methods = ['GET', 'POST'])
def modifydeck():
	deckmdfr = DeckModifier()

	global deck_data
	selectfields = []
	cards = []
	global selected_deck

	for deck in Decks.query.all():
		if deck.name == selected_deck:
			cards = list(eval(deck.cards))


	for field in deckmdfr:
		if field.type == "SelectField":
			selectfields.append(field)

	if deckmdfr.validate_on_submit():
		

		if deckmdfr.deletedeck.data:
			print("Delete")
			Decks.query.filter_by(name = selected_deck).delete()
			db.session.commit()
			return redirect(url_for('selectdeck'))
		else:
			deck=[]
			for field in deckmdfr:
				if field.type == "SelectField":
					deck.append(field.data)

			for userdeck in Decks.query.all():
				if userdeck.name == selected_deck:
					userdeck.cards = str(deck)
			db.session.commit()

		return render_template('modifydeck.html', title='Modify Deck', form=deckmdfr, selecteddeck=selected_deck)


		return render_template('modifydeck.html', title='Modify Deck', form=deckmdfr, selecteddeck=selected_deck)

	elif request.method == 'GET':
		i = 0
		for selectfield in selectfields:
			if i < len(cards):
				selectfield.data = cards[i]
				i += 1

		return render_template('modifydeck.html', title='Modify Deck', form=deckmdfr, selecteddeck=selected_deck)

	return render_template('modifydeck.html', title='Modify Deck', form=deckmdfr, selecteddeck=selected_deck)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	registrationform = RegistrationForm()
	if registrationform.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(registrationform.password.data)
		user = Users(first_name=registrationform.first_name.data, last_name=registrationform.last_name.data, email=registrationform.email.data, password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=registrationform)
def registration():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	user = Users(
		first_name=registrationform.first_name.data,
		last_name=registrationform.last_name.data,
		email=registrationform.email.data,
		password=hashed_pw
		)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	else:
		form = LoginForm()
		if form.validate_on_submit():
			user = Users.query.filter_by(email=form.email.data).first()
			if user and bcrypt.check_password_hash(user.password, form.password.data):
				login_user(user, remember = form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email

	return render_template('account.html', title='Account', form=form)