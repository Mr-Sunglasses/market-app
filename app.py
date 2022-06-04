from flask import Flask, render_template
from data.model import ITEMS

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')


@app.route('/market')
def marketpage():

    return render_template('market.html',items = ITEMS)



if __name__ == "__main__":

    app.run(debug=True)