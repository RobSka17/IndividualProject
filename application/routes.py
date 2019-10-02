from flask import render_template, url_for, redirect
from application import app, db
from application.models import CardStats
from application.forms import SearchByNameForm

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
		for card in unrefinedcards:
			if srchbyname.search_term.data.lower() in card.name.lower():
				for field in srchbyname:
					if field.type == "BooleanField":
						if field.data == True:
							if field.label.text == "Light" or field.label.text == "Dark" or field.label.text == "Fire" or field.label.text == "Water" or field.label.text == "Machine" or field.label.text == "Bug" or field.label.text == "Business" or field.label.text == "Earth":
								if field.label.text.lower() == card.type.lower():
									if card not in cards:
										cards.append(card)
								if field.label.text == "Arachnid" or field.label.text == "Beast" or field.label.text == "Boss" or field.label.text == "Demon" or field.label.text == "Fish" or field.label.text == "Food" or field.label.text == "Good Boi" or field.label.text == "Larva" or field.label.text == "Noble" or field.label.text == "Staff" or field.label.text == "Warrior": 
									if field.label.text.lower() == card.class1.lower() or field.label.text.lower() == card.class2.lower():
										if card not in cards:
											cards.append(card)


		cards_length = len(cards)

		return render_template('byname.html', title='Search by name', form=srchbyname, cards=cards, cardslength=cards_length)
	else:
		return render_template('byname.html', title='Search by name', form=srchbyname)
