# This is a sample Python script.
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import json
from csv import DictReader
import time
import userAgent
import socialLinks as SL
import pickle
import os.path

# object of options class
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# dir_path = os.getcwd()
# options.add_argument(f'user-data-dir={dir_path}/selenium')

browser = webdriver.Chrome("C:\\Projects\\Clickbot\\drivers\\chromedriver.exe", options=options)

# random link selection: links from twitter and facebook
rand_url = random.randrange(1, 4, 1)

# Generate a random number between 1 and 10 to randomly select the article to click
random_element = random.randrange(1, 10, 1)

# Sleep for x number of minutes before you execute the click code. Random between 1 sec and 30 sec
random_time = random.randrange(5, 30, 1)


def startBrowser():
    # function to set the cookies
    # def get_cookies_values(file):
    #     with open(file, encoding='utf-8-sig') as f:
    #         dict_reader = DictReader(f)
    #         list_of_dicts = list(dict_reader)
    #         return list_of_dicts
    #
    #     cookies = get_cookies_values("cookies.csv")
    #
    #     for i in cookies:
    #         browser.add_cookie(i)
    #
    #         browser.refresh()

    # function to continue with the saved session
    # if os.path.exists("cookies.pkl"):
    #     cookies = pickle.load(open("cookies.pkl", "rb"))
    #     for cookie in cookies:
    #         browser.add_cookie(cookie)

    # Press Shift+F10 to execute it or replace it with your code.
    # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    browser.execute_cdp_cmd("Network.setUserAgentOverride", random.choice(userAgent.headers_list))

    # random URL
    url = SL.url
    browser.get(url)

    # browser.get("https://nairobi24.co.ke")
    wait = WebDriverWait(browser, 30)
    # xpath = f"//*[@id='pt-cv-view-6884135wgj']/div/div[{random_element}]/div/h4/a"
    # browser.execute_script("window.ScrollTo(0, document.body.scrollHeight)")

    # sleep the code awaiting another article click.
    time.sleep(random_time)

    # scroll the page to the bottom
    height = browser.execute_script("return document.body.scrollHeight")
    for i in range(height):
        browser.execute_script(f"window.scrollBy(0,{random_time})")

    # find link to the next clickable element
    # elem = wait.until(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, f"//*[@id='pt-cv-view-6884135wgj']/div/div[{random_element}]/div/h4/a")))
    elem = wait.until(expected_conditions.element_to_be_clickable(
        (By.XPATH, f"//*[@id='newsup_posts_list-2']/div/div[2]/div[{random_element}]/ul/li/div[2]/h5/a")))

    # //*[@id="newsup_posts_list-2"]/div/div[2]/div[4]/ul/li/div[2]/h5/a
    # f"//*[@id='newsup_posts_list-2']/div/div[2]/div[{random_element}]/ul/li/div[2]/h5/a"

    elem.click()

    browser.delete_cookie("_ga")
    browser.delete_cookie("_gid")
    browser.delete_cookie("_gat_gtag_UA_80909769_7")
    browser.delete_cookie("_wsm_ref_1_a7d6")
    browser.delete_cookie("_wsm_ses_1_a7d6")
    browser.delete_cookie("_wsm_id_1_a7d6")

    time.sleep(random_time)

    browser.get(url[rand_url])
    # browser.refresh()
