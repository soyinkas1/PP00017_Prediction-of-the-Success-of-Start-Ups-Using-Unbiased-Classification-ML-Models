# Import the required libraries
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataCleaningConfig, DataScrappingConfig


class DataScrapping:
    """"
    This class is used for social media pages scrapping of the organization for enrichment of dataset
    """
    def __init__(self, config: DataScrappingConfig, clean_data_config: DataCleaningConfig):
        self.scrapping_config = config
        self.clean_data_config = clean_data_config

    logging.info("Data scrapper configuration done......")

    # Scrape Twitter
    def twitter_data_scrapping(self):
        """
        The method scrapes the twitter page of the organizations in the database
        return:
        A dataframe containing the tweets
        """
        social_df = pd.read_csv(self.clean_data_config.unclean_backbone_local_data_file,
                                nrows=self.scrapping_config.df_rows)
        logging.info("Twitter url loaded......")
        # Create an empty dictionary to store tweets scraped
        data = {}

        # Helper function to scrape account details of the organisations
        def get_follow():
            time.sleep(10)
            try:
                follower_data = driver.find_element(By.XPATH,
                                                    '//a[contains(@href,"followers")]//span/span').text
                following_data = driver.find_element(By.XPATH,
                                                     '//a[contains(@href,"following")]//span/span').text


            except:
                follow_data = ['following_data', 'follower_data']
                print('error')

            follow_data = [follower_data, following_data]
            logging.info("Twitter followers scrapped......")
            return follow_data

        # Helper function to scrape each post
        def get_tweets(element):
            logging.info("Tweets scrapping ongoing......")
            time.sleep(10)
            try:
                user = element.find_element(By.XPATH, './/span[contains(text(),"@")]').text
                text = element.find_element(By.XPATH, './/div[@lang]').text
                stats = element.find_elements(By.XPATH, './/span[@data-testid]')
                comments_data = stats[0].text
                retweets_data = stats[1].text
                likes_data = stats[2].text

            except:
                tweet_data = ['user', 'text', 'comments', 'retweet', 'likes']

            tweet_data = [user, text, comments_data, retweets_data, likes_data]

            return tweet_data

        time.sleep(10)
        # time.sleep(6)  # this time might vary depending on your computer

        # search_box.send_Keys(Keys.ENTER)
        # Scrape the twitter accounts in a loop
        for twitter_page in social_df[self.scrapping_config.twitter_url]:

            try:
                options = webdriver.ChromeOptions()
                options.add_experimental_option("detach", True)
                # Adding argument to disable the AutomationControlled flag
                options.add_argument("--disable-blink-features=AutomationControlled")
                # Exclude the collection of enable-automation switches
                options.add_experimental_option("excludeSwitches", ['enable-automation'])
                # Turn-off userAutomationExtension
                options.add_experimental_option('useAutomationExtension', False)
                service = Service(executable_path=self.scrapping_config.chrome_driver_path)
                # self.scraper_config.chrome_driver_path)
                driver = webdriver.Chrome(service=service, options=options)
                driver.get(twitter_page)
                driver.maximize_window()
                time.sleep(10)
                try:
                    login_link = driver.find_element(By.XPATH, './/a[@data-testid="login"]')
                    # login_link.click()
                    driver.execute_script("arguments[0].click();", login_link)
                    time.sleep(5)
                    print("finished waiting to open login")
                    # wait of 6 seconds to let the page load the content
                    time.sleep(8)  # this time might vary depending on your computer

                except:
                    pass
                # locating username and password inputs and sending text to the inputs
                time.sleep(8)
                username = driver.find_element(By.XPATH, '//input[@autocomplete ="username"]')
                username.send_keys(self.scrapping_config.twitter_username)  # Write Email Here
                # Clicking on "Next" button
                next_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Next"]')
                next_button.click()
                # wait of 2 seconds after clicking button
                time.sleep(2)
                # Enter the password
                password = driver.find_element(By.XPATH, '//input[@autocomplete ="current-password"]')
                password.send_keys(self.scrapping_config.twitter_password)  # Write Password Here
                # locating login button and then clicking on it
                login_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Log in"]')
                login_button.click()
                # Get details of the Twitter account
                # following_data = []
                # follower_data = []

                follow_data = get_follow()
                follower_data = follow_data[0]
                following_data = follow_data[1]

                # Refresh the page by searching for tweet mentions of the organisation
                name = twitter_page.split('/')
                name = name[-1]
                search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
                search_box.send_keys(name, Keys.ENTER)
                time.sleep(15)
                # Create list to store the tweet details
                user_data = []
                texts = []
                comment_data = []
                retweet_data = []
                like_data = []
                tweet_ids = set()

                # Scrape the tweets by scrolling infinitely
                scrolling = True
                while scrolling:
                    tweets = WebDriverWait(driver, 8).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))
                    for tweet in tweets[:-self.scrapping_config.max_tweets]:
                        tweet_data = get_tweets(tweet)
                        tweet_id = ''.join(tweet_data)
                        if tweet_id not in tweet_ids:
                            tweet_ids.add(tweet_id)
                            user_data.append(tweet_data[0])
                            texts.append(" ".join(tweet_data[1].split()))
                            comment_data.append(tweet_data[2])
                            retweet_data.append(tweet_data[3])
                            like_data.append(tweet_data[4])
                            # view_data.append(tweet_data[5])
                    last_height = driver.execute_script("return document.body.scrollHeight")

                    while True:
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(2)
                        new_height = driver.execute_script("return document.body.scrollHeight")

                        # Set maximum tweets
                        if new_height == last_height or len(user_data) > self.scrapping_config.max_tweets:
                            scrolling = False
                            break
                        else:
                            last_height = new_height
                            break
                # Add tweets details to a DataFrame
                tweet_df = pd.DataFrame(
                    {'account': twitter_page, 'user': user_data, 'text': texts, 'comments': comment_data,
                     'retweets': retweet_data, 'likes': like_data,
                     'follower_data': follower_data, 'following_data': following_data})

                # Add the DataFrame to a dictionary
                data[f"{name}"] = tweet_df

                driver.quit()
            except Exception as e:
                raise CustomException(e, sys)

        # Create the folder for scraped tweets if it is not existing
        os.makedirs(os.path.dirname(self.scrapping_config.root_dir), exist_ok=True)
        # Save each DataFrame as a csv file for each entity
        for key, val in data.items():
            val.to_csv(os.path.join(self.scrapping_config.root_dir, "{}.csv".format(str(key))))

        logging.info("Tweets scrapping completed......")


# Scrape Facebook

    # def facebook_data_scrapping(self):
    #
    #     """
    #         The method scrapes the facebook page of the organizations in the database
    #         return:
    #         A dataframe containing the tweets
    #     """
    #    # Import the dataset containing the twitter accounts to scrape
    #     social_df = pd.read_csv(self.clean_data_config.unclean_backbone_local_data_file,
    #                             nrows=self.scrapping_config.df_rows)
    #     print(social_df.head(3))
    #     logging.info("Facebook url loaded......")
    #
    #
    #
    #
    #
    #     # Create the folder for scraped tweets if it is not existing
    #     os.makedirs(os.path.dirname(self.scrapping_config.root_dir), exist_ok=True)
    #     # Save each DataFrame as a csv file for each entity
    #     for key, val in data.items():
    #         val.to_csv(os.path.join(self.scrapping_config.root_dir, "{}.csv".format(str(key))))
    #
    #     logging.info("Facebbok scrapping completed......")

# Scrape LinkedIn




