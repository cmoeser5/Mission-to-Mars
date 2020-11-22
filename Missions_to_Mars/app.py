from scrape_mars import scrape, mars
from scrape_mars import firefox_driver
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import os

driver = firefox_driver()
app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars= mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect ("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)