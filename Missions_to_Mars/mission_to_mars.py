# set up and dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#set up driver
options = Options()
options.headless = True
driver = webdriver.Chrome("/Users/carolinemoeser/Downloads/chromedriver", options=options)

# NASA Mars News

# establish url and scrape web page
url = "https://mars.nasa.gov/news/"

driver.get(url)
driver.implicitly_wait(10)
html = driver.page_source

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

# extract news titles
news_titles = soup.find_all("li", class_="slide")

# extract latest news title and assign to variable
latest = news_titles[0].find("div", class_="content_title")
news_title = latest.text.strip()

# extract latest news paragraph text and assign to variable
p_text = news_titles[0].find("div", class_="article_teaser_body")
news_p = p_text.text.strip()

print("NASA Mars News")
print("-" * 30)
print(news_title)
print(news_p)

# JPL Mars Space Images - Featured Image

# establish url and go seach Mars images
base_url = "https://www.jpl.nasa.gov"
url = base_url + "/spaceimages/?search=&category=Mars"

driver.get(url)
driver.implicitly_wait(10)

# navigate web page to find large image url
driver.find_element_by_link_text("FULL IMAGE").click()
driver.find_element_by_partial_link_text("more info").click()

# scrape page
driver.implicitly_wait(10)
html = driver.page_source

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

main_img = soup.find_all("img", class_="main_image")

# extract out src attribute
src = ""

for image in main_img:
    src = image["src"]

# combine base url with src string and assign to variable
featured_image_url = base_url + src

print("Featured Mars Image URL")
print("-" * 30)
print(featured_image_url)

# Mars Facts

# establish url and scrape web page
url = "https://space-facts.com/mars/"

driver.get(url)
driver.implicitly_wait(10)
html = driver.page_source

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

tables = soup.find_all("table")

# index for info only on the mars facts table
facts_table = tables[0]

# extract data from the facts table
table_data = [[cell.text for cell in row.find_all(["th", "td"])] for row in facts_table.find_all("tr")]

# convert to dataframe
df = pd.DataFrame(table_data)

#save html of table to a string
mars_table = df.to_html(index=False)

print("Mars Facts Table")
print("-" * 30)
print(df)

# Mars Hemispheres 

# establish url and scrape web page
base_url = "https://astrogeology.usgs.gov"
url = base_url + "/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

driver.get(url)
driver.implicitly_wait(10)
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

# remove all h3 tags from list
titles = [h3.text.strip() for h3 in soup.find_all("h3")]

# loop through list of titles to navigate to each page and extract html from each
html_pages = []
for title in titles:
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(title).click()
    driver.implicitly_wait(10)
    html_pages.append(driver.page_source)

# convert list into a string for bs4
html = " ".join(map(str, html_pages))

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

img_urls = soup.find_all("img", class_="wide-image")

# extract all src attributes
img_srcs = []
for img in img_urls:
    img_srcs.append(img["src"])

# add base url to img_srcs
urls = [(base_url + e) for e in img_srcs]

# zip lists together in tuples for converting to list of dicts
tuple_list = list(zip(titles, urls))

# keys for list of dictionaries for each hemisphere
keys = ("title", "img_url")

# zip the list of keys and values together for each tuple in the list
hemisphere_img_urls = [dict(zip(keys, values)) for values in tuple_list]

print("Mars Hemispheres")
print("-" * 30)
print(hemisphere_img_urls)