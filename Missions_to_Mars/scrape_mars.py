from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests


def scrape_data():
    # NASA Mars News
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url_news = 'https://redplanetscience.com/'
    browser.visit(url_news)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('div', class_='list_text')
    latest_news_title = news[0].find('div', class_='content_title').text
    latest_news_p = news[0].find('div', class_='article_teaser_body').text
    browser.quit()

    # Mars Image
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url_image = 'https://spaceimages-mars.com/'
    browser.visit(url_image)  
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')                      
    featured_image = soup.find_all('img', class_='headerimage fade-in')
    featured_image_url_part = featured_image[0]['src']
    featured_image_url = url_image + featured_image_url_part
    browser.quit()

    # Mars Facts
    import pandas as pd
    url_fact = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url_fact)
    df = tables[0]
    df.columns = ['', 'Mars', 'Earth']
    df.loc[-1] = ['Description',"",""]
    df.sort_index(inplace=True)
    html_table = df.to_html(index=False)
    html_table = html_table.replace('border="1"', 'border=3 class="table table-striped table table-bordered"').replace('right','left')

    # Mars Hemispheres 
    url_hemispheres = 'https://marshemispheres.com/'
    response = requests.get(url_hemispheres)
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    ## Loop through returned results
    for result in results:
        title = result.find('h3').text
        thumb_link = result.find('a')['href']
        full_thumb_link = url_hemispheres + thumb_link
        response = requests.get(full_thumb_link)
        soup = BeautifulSoup(response.text, 'lxml')
        img_link = soup.find_all('img', class_='wide-image')[0]['src']
        full_img_link = url_hemispheres + img_link
        hemisphere_dict = {
                "title": title,
                "img_url": full_img_link
                }
        hemisphere_image_urls.append(hemisphere_dict)

    # Store data in a dictionary
    mars_data = {
        "latest_news_title": latest_news_title,
        "latest_news_p": latest_news_p,
        "featured_image_url": featured_image_url,
        "html_table":html_table,
        "hemisphere_image_urls":hemisphere_image_urls
    }

    # Return results
    return mars_data