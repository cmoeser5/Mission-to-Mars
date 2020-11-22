import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Define Firefox Webdriver 
def firefox_driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    return driver

driver = firefox_driver()
mars= {}

# Define scrape function
def scrape(driver):
    # Mars News Site
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Finding News
    news_titles = soup.find_all("li", class_="slide")
    latest_story = news_titles[1].find("div", class_="content_title")
    mars["news_title"] = latest_story.text.strip()

    article_p = news_titles[1].find("div", class_="article_teaser_body")
    mars["news_article_p"] = article_p.text.strip()

    # JPL Mars Space Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    image = soup.find("article")["style"].replace('background-image: url(','').replace(');', '')[1:-1]
    main_url = "https://www.jpl.nasa.gov"
    image_url = main_url + image
    mars["featured_image"] = image_url

    # Mars Facts Table
    page = requests.get("https://space-facts.com/mars")
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all("table")

    # Convert table into DataFrame using Pandas
    table = tables[0]
    table_data = [
    [cell.text for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")
    ]
    df = pd.DataFrame(table_data)
    mars_html_table = df.to_html(index=False)
    mars["mars_facts"] = mars_html_table

    # Mars Hemispheres
    # Image 1
    def get_html_h1(url_h1):
        driver = webdriver.Firefox()
        driver.get(url_h1)
        html_h1 = driver.page_source
        driver.close()
        return html_h1

    url_h1 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    html_h1 = get_html_h1(url_h1)
    soup_h1 = BeautifulSoup(html_h1, "html.parser")
    image_h1 = soup_h1.find("div", class_ = "downloads").find("a")["href"]

    #Image 2
    def get_html_h2(url_h2):
        driver = webdriver.Firefox()
        driver.get(url_h2)
        html_h2 = driver.page_source
        driver.close()
        return html_h2

    url_h2 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    html_h2 = get_html_h2(url_h2)
    soup_h2 = BeautifulSoup(html_h2, "html.parser")
    image_h2 = soup_h2.find("div", class_ = "downloads").find("a")["href"]

    #Image 3
    def get_html_h3(url_h3):
        driver = webdriver.Firefox()
        driver.get(url_h3)
        html_h3 = driver.page_source
        driver.close()

        return html_h3

    url_h3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    html_h3 = get_html_h3(url_h3)
    soup_h3 = BeautifulSoup(html_h3, "html.parser")
    image_h3 = soup_h3.find("div", class_ = "downloads").find("a")["href"]

    #Image 4
    def get_html_h4(url_h4):
        driver = webdriver.Firefox()
        driver.get(url_h4)
        html_h4 = driver.page_source
        driver.close()

        return html_h4

    url_h4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    html_h4 = get_html_h3(url_h4)
    soup_h4 = BeautifulSoup(html_h4, "html.parser")
    image_h4 = soup_h4.find("div", class_ = "downloads").find("a")["href"]

    #Image Dictionary
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": "image_h1"},
        {"title": "Schiaparelli Hemisphere", "img_url": "image_h2"},
        {"title": "Syrtis Major Hemisphere", "img_url": "image_h3"},
        {"title": "Valles Marineris Hemisphere", "img_url": "image_h4"},
    ]
    mars["mars hemispheres"] = hemisphere_image_urls

    return mars
    driver.close()

scrape(driver)
print(mars)

if __name__ == "__main__":
    print(scrape(driver))