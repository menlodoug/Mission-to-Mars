# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def scrape_all():
   # Initiate headless driver for deployment
   browser = Browser("chrome", executable_path="chromedriver", headless=True)
   news_title, news_paragraph = mars_news(browser)
   # Run all scraping functions and store results in dictionary
   data = {"news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "hemispheres": mars_hemispheres(browser),
      "last_modified": dt.datetime.now()}
   browser.quit()
   return data
   
def mars_news(browser):

   # Visit the mars nasa news site
   url = 'https://mars.nasa.gov/news/'
   browser.visit(url)
   # Optional delay for loading the page
   browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = BeautifulSoup(html, 'html.parser')

   # Add try/except for error handling
   try:
       slide_elem = news_soup.select_one('ul.item_list li.slide')
       # Use the parent element to find the first <a> tag and save it as `news_title`
       news_title = slide_elem.find("div", class_='content_title').get_text()
       # Use the parent element to find the paragraph text
       news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
       return news_title, news_p
   except AttributeError:
       return None, None

def featured_image(browser):
    # "### Featured Images"
    # # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
        img_url_rel
        
        # Use the base URL to create an absolute URL
        img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
        return img_url
        
    except AttributeError:
            return None

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[1]

    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

def mars_hemispheres(browser):
    # Add try/except for error handling
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    hemi_soup = BeautifulSoup(html, 'html.parser')
    list_link = []
    for link in hemi_soup.select('div.description a[href]'):
        ("https://astrogeology.usgs.gov{}".format(link['href']))
        list_link.append(("https://astrogeology.usgs.gov{}".format(link['href'])))
    
    url = list_link[0]
    browser.visit(url)
    html = browser.html
    cerberus_soup = BeautifulSoup(html, 'html.parser')
    cerb_url_rel = cerberus_soup.select_one('img.wide-image').get("src")
    cerb_img_url = f'https://astrogeology.usgs.gov{cerb_url_rel}'
    cerb_title = cerberus_soup.find('h2')
    cerb_title.text

    url = list_link[1]
    browser.visit(url)
    html = browser.html
    schia_soup = BeautifulSoup(html, 'html.parser')
    schia_url_rel = schia_soup.select_one('img.wide-image').get("src")
    schia_img_url = f'https://astrogeology.usgs.gov{schia_url_rel}'
    schia_title = schia_soup.find('h2')
    schia_title.text

    url = list_link[2]
    browser.visit(url)
    html = browser.html
    syrtis_soup = BeautifulSoup(html, 'html.parser')
    syrtis_url_rel = syrtis_soup.select_one('img.wide-image').get("src")
    syrtis_img_url = f'https://astrogeology.usgs.gov{syrtis_url_rel}'
    syrtis_title = syrtis_soup.find('h2')
    syrtis_title.text

    url = list_link[3]
    browser.visit(url)
    html = browser.html
    valles_soup = BeautifulSoup(html, 'html.parser')
    valles_url_rel = valles_soup.select_one('img.wide-image').get("src")
    valles_img_url = f'https://astrogeology.usgs.gov{valles_url_rel}'
    valles_title = valles_soup.find('h2')
    valles_title.text

    return cerb_img_url, cerb_title.text, schia_img_url, schia_title.text, syrtis_img_url, syrtis_title.text, valles_img_url, valles_title.text

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())