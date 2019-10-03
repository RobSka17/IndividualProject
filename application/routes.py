from flask import render_template, url_for, redirect
from application import app, db
from application.models import CardStats, Decks
from application.forms import SearchByNameForm, DeckBuilder, DeckModifier

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
		newdeck = Decks(name = deckbldr.deckname.data, cards=str(deck))
		db.session.add(newdeck)
		db.session.commit()

		yourdeck = list(eval(newdeck.cards))

		return render_template('builddeck.html', title='Search by name', form=deckbldr, cardnumber=cardnumber, yourdeck=yourdeck)
	else:
		return render_template('builddeck.html', title='Search by name', form=deckbldr, cardnumber=cardnumber)

@app.route('/modify_a_deck', methods=['GET', 'POST'])
def modifydeck():
	deckmdfr = DeckModifier()
	decks = []
	deck_cards = []
	if deckmdfr.is_submitted():

		if deckmdfr.search_all_check.data == True:
				for deck in Decks.query.all():
					decks.append(deck)
		else:
			for deck in Decks.query.all():
				if deckmdfr.decksearch.data.lower() in deck.name.lower():
					decks.append(deck)

		for deck in decks:
			deck_cards.append(list(eval(deck.cards)))

		i = 0
		for field in deckmdfr:
			if field.type == "SelectField":
				while i < len(deck_cards):
					for card in deck_cards:
						print(card[i])
						field.default = card[i]
						i += 1
						

	return render_template('modifydeck.html', title='Existing Decks', form=deckmdfr, decks=decks, deckcards=deck_cards)