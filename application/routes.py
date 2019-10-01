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
	unrefinedcards = cardstats.query.filter_by(name=srchbyname.search_term.data).all()
	cards = []
	for card in unrefinedcards:
		if srchbyname.search_term.data in card.name:
			cards.append(card)

	return render_template('byname.html', title='Search by name', form=srchbyname, cards=cards)
