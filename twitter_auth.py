from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import csv

def scrape_tweets(username, tweet_count):
    # Set up Selenium WebDriver
    service = Service('./chromedriver')
    driver = webdriver.Chrome(service=service)

    try:
        # Open Twitter profile
        url = f"https://twitter.com/{username}"
        driver.get(url)
        time.sleep(5)  # Allow time for the page to load

        # Scroll down to load tweets
        for _ in range(10):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(3)

        # Find tweet text elements
        tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweet"]//span')
        print(f"Found {len(tweets)} tweets.")

        # Save tweets to a CSV file
        with open(f'{username}_tweets.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tweet Text"])

            for tweet in tweets[:tweet_count]:
                writer.writerow([tweet.text])

        print(f"Saved {min(tweet_count, len(tweets))} tweets to {username}_tweets.csv")

        input("Press Enter to close the browser...")


    except Exception as e:
        print(f"Error: {e}")
    finally:
        input("Press Enter to close the browser...")
        driver.quit()


# Call the function to scrape tweets
scrape_tweets("elonmusk", 10)  # Scrape 10 tweets
