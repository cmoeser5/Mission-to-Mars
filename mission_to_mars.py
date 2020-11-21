import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Create a function to get the HTML from the URL
def get_html(url):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    driver.get(url)
    html = driver.page_source
    driver.close()

    return html

# Mars News Site URL
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
html = get_html(url)

soup = BeautifulSoup(html, "html.parser")

# Find the latest story and title from the page
news_titles = soup.find_all("li", class_="slide")
latest_story = news_titles[1]

print(
    {
        "article_title": latest_story.find("h3").text.strip(),
        "article_p": latest_story.find(
            "div", class_="article_teaser_body"
        ).text.strip(),
    }
)

# JPL Mars Space Images - Featured Image
def get_image(url):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    driver.get(url)
    driver.find_element_by_link_text("FULL IMAGE").click()
    driver.find_elements_by_partial_link_text("more info").click()
    html=driver.page_source
    driver.close()
    
    return html

# JPL Mars Space Image URL
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
html = get_image(url)

soup = BeautifulSoup(html, "html.parser")

main_image = soup.find_all("img", class_="main_image")

src = ""
for image in main_image:
    src = image["src"]

featured_image_url = "https://www.jpl.nasa.gov" + src
print(featured_image_url) 