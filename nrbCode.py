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


class Clickbot:
    # object of options class
    # def __init__(self, options, browser):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # dir_path = os.getcwd()
    # options.add_argument(f'user-data-dir={dir_path}/selenium')
    global browser
    browser = webdriver.Chrome("C:\\Projects\\Clickbot\\drivers\\chromedriver.exe", options=options)

    # random link selection: links from twitter and facebook
    global rand_url
    rand_url = random.randrange(1, 17, 1)

    # Generate a random number between 1 and 10 to randomly select the article to click
    global random_element
    random_element = random.randrange(1, 10, 1)

    # Sleep for x number of minutes before you execute the click code. Random between 1 sec and 30 sec
    global random_time
    random_time = random.randrange(5, 30, 1)

    # global count
    global count
    count = 0

    def startbrowser(self):
        # Press Shift+F10 to execute it or replace it with your code.
        # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
        browser.execute_cdp_cmd("Network.setUserAgentOverride", random.choice(userAgent.headers_list))

    def gotourl(self):
        # random URL
        rnd = random.randrange(1, 16, 1)
        link = SL.url
        browser.get(link[rnd])

        # browser.get("https://nairobi24.co.ke")
        global wait
        wait = WebDriverWait(browser, 120)
        # xpath = f"//*[@id='pt-cv-view-6884135wgj']/div/div[{random_element}]/div/h4/a"
        # browser.execute_script("window.ScrollTo(0, document.body.scrollHeight)")

        # sleep the code awaiting another article click.
        time.sleep(random_time)

    def scrollthepage(self):
        # scroll the page to the bottom
        height = browser.execute_script("return document.body.scrollHeight")
        for i in range(height):
            browser.execute_script(f"window.scrollBy(0,{random_element / 2})")

    def clickfirstelem(self):
        rnd3 = random.randrange(1, 10, 1)
        # find link to the next clickable element
        # elem = wait.until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, f"//*[@id='pt-cv-view-6884135wgj']/div/div[{random_element}]/div/h4/a")))
        elem = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, f"//*[@id='newsup_posts_list-2']/div/div[2]/div[{rnd3}]/ul/li/div[2]/h5/a")))

        # //*[@id="newsup_posts_list-2"]/div/div[2]/div[4]/ul/li/div[2]/h5/a
        # f"//*[@id='newsup_posts_list-2']/div/div[2]/div[{random_element}]/ul/li/div[2]/h5/a"

        elem.click()

    def clearcookies(self):
        browser.delete_cookie("_ga")
        browser.delete_cookie("__gads")
        browser.delete_cookie("test_cookie")
        browser.delete_cookie("_gid")
        browser.delete_cookie("_gat_gtag_UA_80909769_7")
        browser.delete_cookie("_wsm_ref_1_a7d6")
        browser.delete_cookie("_wsm_ses_1_a7d6")
        browser.delete_cookie("_wsm_id_1_a7d6")

        # browser.execute_script('window.localStorage.removeItem("google_experiment_mod57");')
        # browser.execute_script('window.localStorage.removeItem("google_experiment_mod37");')
        # browser.execute_script('window.localStorage.removeItem("google_experiment_mod56");')
        # browser.execute_script('window.localStorage.removeItem("google_experiment_mod36");')
        # browser.execute_script('window.localStorage.removeItem("google_experiment_mod53");')
        # browser.execute_script('window.localStorage.removeItem("google_experiment_mod44");')
        # browser.execute_script('window.localStorage.removeItem("google_experiment_mod34");')
        # browser.execute_script('window.localStorage.removeItem("goog_pem_mod");')
        # browser.execute_script('window.localStorage.removeItem("rc::e");')

        time.sleep(random_time)

    def restartsession(self):
        rnd2 = random.randrange(1, 17, 1)
        url = SL.url
        browser.get(url[rnd2])
        # browser.refresh()


while count < 500:
    # cycle = count / 5
    start = Clickbot()
    start.startbrowser()
    start.gotourl()
    if count % 3 != 0:
        start.scrollthepage()
    if count % 3 != 0:
        start.clickfirstelem() #pick a random link
    # start.clearcookies()
    start.restartsession()
    # time.sleep(random.randrange(5, 60, 1))
    start.clearcookies()
    count += 1
    print(count)
