from scrape_mars import scrape, mars_dict
from scrape_mars import firefox_driver
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import os

driver = firefox_driver()

app = Flask(__name__)
CONN = "mongodb://localhost:27017/mars_dict"
app.config["MONGO_URI"] = CONN

mongo = PyMongo(app)


@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars_dict=mars_dict)

@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars_dict
    mongo.db.mars_dict.drop()
    mongo.db.mars_dict.insert_one(scrape(driver))
    mars_dict.update({},mars_dict, upsert=True)
    return redirect ("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)