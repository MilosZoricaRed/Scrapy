from flask import Flask
from flask import jsonify
from scraping import scrape

app = Flask(__name__)


@app.route('/scrapy')
def index():
    return jsonify(Jobs=scrape())



if __name__ == "__main__":
    app.run(debug=True)
