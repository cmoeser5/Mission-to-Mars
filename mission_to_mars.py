import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Create a function to get the HTML from the URL
# def get_html(url):
#     fireFoxOptions = webdriver.FirefoxOptions()
#     fireFoxOptions.set_headless()
#     driver = webdriver.Firefox(firefox_options=fireFoxOptions)
#     driver.get(url)
#     html = driver.page_source
#     driver.close()

#     return html

# # Mars News Site URL
# url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
# html = get_html(url)

# soup = BeautifulSoup(html, "html.parser")

# # Find the latest story and title from the page
# news_titles = soup.find_all("li", class_="slide")
# latest_story = news_titles[1]

# print(
#     {
#         "article_title": latest_story.find("h3").text.strip(),
#         "article_p": latest_story.find(
#             "div", class_="article_teaser_body"
#         ).text.strip(),
#     }
# )

# JPL Mars Space Images - Featured Image
# def get_image(url):
#     fireFoxOptions = webdriver.FirefoxOptions()
#     fireFoxOptions.set_headless()
#     driver = webdriver.Firefox(firefox_options=fireFoxOptions)
#     driver.get(url_image)
#     driver.find_element_by_link_text("FULL IMAGE").click()
#     driver.find_elements_by_class_name("button").click()
#     html_image=driver.page_source
#     driver.close()
    
#     return html_image

# JPL Mars Space Image URL
# url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# html_image = get_image(url_image)

# soup_image = BeautifulSoup(html, "html.parser")

# main_image = soup_image.find_all("img", class_="main_image")

# src = ""
# for image in main_image:
#     src = image["src"]

# featured_image_url = f"https://www.jpl.nasa.gov" + f"{src}"
# print(featured_image_url) 

# Mars Facts
# page = requests.get("https://space-facts.com/mars")
# soup_facts = BeautifulSoup(page.content, "html.parser")
# tables = soup_facts.find_all("table")

# Convert the table to a pandas DataFrame
# table = tables[0]
# table_data = [
#     [cell.text for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")
# ]
# df = pd.DataFrame(table_data)
# mars_html_table = df.to_html(header=False, index=False)

# Mars Hemispheres
# Image 1
def get_html_h1(url_h1):
    driver = webdriver.Firefox()
    driver.get(url_h1)
    html_h1 = driver.page_source
    driver.close()

    return html_h1

