import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def scrape_dev_dot_to(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get(url)

    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='article-652398']/div/div/div[1]/div/div[1]/a/img")
            )
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    # find all the article elements
    article_elements = browser.find_elements_by_tag_name('article')
    for article in article_elements:
        print(article)
        # selenium.webdriver.remote.webelement.WebElement object
        # print(article.get_attribute('class'))
        # crayons-story
        article_title = article.find_element_by_tag_name('a')
        print(article_title)

        article_title_link = article_title.get_attribute('href')
        print(article_title_link)

        article_title_text = (article_title.get_attribute('innerHTML')).strip()
        print(article_title_text)
        # print(type(article_title_text))
        # print(len(article_title_text))

        article_timestamp = article.find_element_by_tag_name('time')
        article_timestamp_text = (article_timestamp.get_attribute('innerHTML')).strip()
        print(article_timestamp_text)
        # print(type(article_timestamp_text))
        # print(len(article_timestamp_text))

    print(len(article_elements))
