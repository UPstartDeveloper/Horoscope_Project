from flask import Flask, request
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
    return """
    <form action='/horoscope'>
        <p>
            What is your name?
            <input type="text" name="name"/>
        </p>
        <p>
            <input type="checkbox" name="show_horoscopes"/>
            Show Horoscopes
        </p>
        <p>
            How many horoscopes do you want?
            <select name="num_horoscopes">
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
                <option value="4">Four</option>
                <option value="5">Five</option>
                <option value="6">Six</option>
            </select>
        </p>
        <input type="submit">
    </form>
    """


@app.route('/horoscope')
def get_horoscope():
    """Give the user a horoscope"""
    name = request.args.get('name')
    num_horoscopes = int(request.args.get('num_horoscopes'))
    show_horoscopes = request.args.get('show_horoscopes')
    predictions = ', '.join(sample(horoscopes, num_horoscopes))

    if show_horoscopes:
        return f"Hello there, {name}: {predictions}."
    else:
        return f"Hello there, {name}! Have a nice day!"


if __name__ == "__main__":
    app.run(debug=True)
