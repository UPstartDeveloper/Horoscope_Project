from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)

horoscopes = [
    'your day will be awesome',
    'your day will be terrific',
    'your day will be fantastic',
    'neato, you have a fantabulous day ahead',
    'your day will be oh-so-not-meh',
    'this day will be brilliant',
    'looks like today is just ducky',
    'I proclaim your day to be INCREDIBLE',
    'this day will be wonderful',
    'smash this day',
    'this day shall be lovely',
    'your day will be just satenacious']


@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')


@app.route('/horoscope')
def get_horoscope():
    """Give the user a horoscope"""
    name = request.args.get('name')
    num_horoscopes = int(request.args.get('num_horoscopes'))
    show_horoscopes = request.args.get('show_horoscopes')
    horoscopes_to_show = sample(horoscopes, num_horoscopes)
    # predictions = ', '.join(sample(horoscopes, num_horoscopes))

    return render_template(
        'horoscopes.html',
        name=name,
        show_horoscopes=show_horoscopes,
        horoscopes_to_show=horoscopes_to_show))

"""
    if show_horoscopes:
        return f"Hello there, {name}: {predictions}."
    else:
        return f"Hello there, {name}! Have a nice day!"
"""

if __name__ == "__main__":
    app.run(debug=True)
