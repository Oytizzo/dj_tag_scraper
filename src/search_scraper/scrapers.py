import datetime
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.utils import timezone

from .models import SearchItem, ScrapeRecord


def scrape_dev_dot_to(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get(url)

    timeout = 10

    try:
        # for django
        # /html/body/div[9]/div/main/div[2]/div[2]/div[2]/article[1]

        # for react
        # /html/body/div[9]/div/main/div[2]/div[2]/div[2]/article[1]
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[9]/div/main/div[2]/div[2]/div[2]/article[1]")
            )
        )

        scrape_record = ScrapeRecord.objects.create(
            finish_time=timezone.now()
        )
        # find all the article elements -> using 'article' tag
        article_elements = browser.find_elements_by_tag_name('article')
        for article in article_elements:
            # check if the article exist for a user
            if article.get_attribute('data-content-user-id') != 'undefined':

                # find all the article tag -> using 'a' tag in article -> chaining the find
                article_title = article.find_element_by_tag_name('a')

                # get the 'href' attribute from the anchor tag
                article_title_link = article_title.get_attribute('href')
                print(article_title_link)

                # get the title or innerHTML of the anchor tag and strip blank spaces
                article_title_text = (article_title.get_attribute('innerHTML')).strip()
                print(article_title_text)

                # get the 'time' tag object
                article_timestamp = article.find_element_by_tag_name('time')

                # get the time str from the object and strip blank spaces
                article_timestamp_text = (article_timestamp.get_attribute('innerHTML')).strip()
                print(article_timestamp_text)

                # convert the news_item_time into python date object
                if "'" in article_timestamp_text:
                    # parse the year
                    article_date = datetime.datetime.strptime(article_timestamp_text, "%b %d '%y").date()

                else:
                    # the year is the current year
                    article_date = datetime.datetime.strptime(article_timestamp_text, "%b %d")
                    today = datetime.date.today()
                    article_date = article_date.replace(year=today.year).date()

                # no articles older than 2 years
                two_years_ago = datetime.date.today() - relativedelta(years=2)

                if article_date > two_years_ago:
                    SearchItem.objects.get_or_create(
                        title=article_title_text,
                        link=article_title_link,
                        source='dev.to',
                        publish_date=article_date,
                    )

        print(len(article_elements))

        scrape_record.finish_time = timezone.now()
        scrape_record.finished = True
        scrape_record.save()

    except TimeoutException:
        print("Timed out waiting for page to load")

    except Exception as e:
        print(e)
    finally:
        browser.quit()
