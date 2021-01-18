
# set up and dependencies
from scrape_mars import scrape
from scrape_mars import configure_chrome_driver
import os
from flask import Flask, render_template, redirect
import pymongo

driver = configure_chrome_driver()

# set up connections to Mongo Database
CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.mars

app = Flask(__name__)

@app.route("/")
def main():

    mars_data = db.mars.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape_route():
    db.mars.drop()
    db.mars.insert_one(scrape(driver))
    return redirect("/", code=303)


if __name__ == "__main__":
    app.run(debug=True)