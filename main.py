# This is a sample Python script.

from selenium import webdriver
import os, random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import csv
# from selenium.webdriver.
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
    # DesiredCapabilities capabilities = new DesiredCapabilities()
    options.set_capability("deviceOrientation", "landscape")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    global browser
    browser = webdriver.Chrome("C:\\Projects\\Clickbot\\drivers\\chromedriver.exe", options=options)

    # random link selection: links from twitter and facebook
    global rand_url
    rand_url = random.randrange(1, 17, 1)

    # Generate a random number between 1 and 10 to randomly select the article to click
    global random_element
    random_element = random.randrange(0, 6, 1)

    # Sleep for x number of minutes before you execute the click code. Random between 1 sec and 30 sec
    global random_time
    random_time = random.randrange(5, 30, 1)

    # global count
    global count
    count = 0

    global timezones
    timezones = [
        "America/Chicago",
        "America/New_York",
        "America/Los_Angeles",
        "US/Eastern",
        "America/Phoenix",
        "America/Guatemala",
        "America/Detroit",
        "America/Denver",
        "America/Cambridge_Bay",
        "America/Belize",
    ]

    global resolutions
    resolutions = [
        '480x800', #
        '360x740', #Samsung galaxy s9
        '480x853', #Samsung galaxy note 9
        '600x960',
        '360x800',
        '360x820',
        '360x780',
        '360x720',
        '337x512',
        '360x640',
        '320x534',
        '412x869',
        '412x846',
        '428x926',
        '414x896',
        '390x844'
    ]

    global user_agent
    user_agent = random.choice(userAgent.headers_list)

    def startbrowser(self):
        # Press Shift+F10 to execute it or replace it with your code.
        # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
        browser.execute_cdp_cmd("Network.setUserAgentOverride", user_agent)
        tz_params = {'timezoneId': random.choice(timezones)}
        # print(user_agent)
        browser.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)

    def gotourl(self):
        # random URL
        global wait
        wait = WebDriverWait(browser, 120)

        rnd = random.randrange(0, 10, 1)
        link = SL.url
        browser.get(link[rnd])
        # sleep the code awaiting another article click.
        time.sleep(random_time)

    def scrollthepage(self, counted):
        # scroll the page to the bottom
        browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/10))")
        time.sleep(random.randrange(1, 5))
        browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/8))")
        time.sleep(random.randrange(4, 10))
        browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/6))")
        time.sleep(random.randrange(1, 7))
        browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*2/5))")
        time.sleep(random.randrange(1, 5))
        browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2))")
        time.sleep(random.randrange(5, 10))
        browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4))")
        time.sleep(random.randrange(1, 3))
        if counted % 3 == 0:
            browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/4))")


    def clickfirstelem(self, count_val):
        # TOP NEWS BLOCK
        rnd3 = random.randrange(1, 10, 1)
        # YOU MISSED BLOCK
        rnd4 = random.randrange(1, 5, 1)

        if count_val % 3 == 0:
            elem = wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, f"//*[@id='newsup_posts_list-2']/div/div[2]/div[{rnd3}]/ul/li/div[2]/h5/a")))
        else:
            elem = wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, f"// *[ @ id = 'block-3'] / div / div / ul / li[{rnd4}] / a")))

        webdriver.ActionChains(browser).click(elem).perform()
        # elem.click()

    def clearcookies(self):
        WebDriverWait(browser, 120)
        browser.delete_all_cookies()
        browser.execute_script('window.localStorage.clear();')
        # browser.set

    def restartsession(self):
        rnd2 = random.randrange(12, 17, 1)
        url = SL.url
        browser.get(url[rnd2])
        # browser.refresh()

    def savecookies(self):
        WebDriverWait(browser, 120)
        rand_count = random.randrange(10, 99, 1)
        # ua = browser.execute_script("return navigator.userAgent")
        cookies = browser.get_cookies()
        keys = cookies[0].keys()
        keys2 = ['userAgent']
        with open(f'cookies/cookies-{rand_count}.csv', 'w', encoding='UTF8', newline='') as f:
            doc = csv.DictWriter(f, fieldnames=keys)
            doc.writeheader()
            doc.writerows(cookies)

        with open(f'uagents/ua-{rand_count}.csv', 'w', encoding='UTF8', newline='') as f:
            doc2 = csv.DictWriter(f, fieldnames=keys2)
            doc2.writeheader()
            doc2.writerow(user_agent)

    def retrievecookies(self):
        # get the cookies file
        file = random.choice(os.listdir("C:\\Projects\Clickbot\cookies"))
        # retrieve the filename
        filename = os.path.basename(file)
        # get the random value generated from end of the file
        randvalue = filename[-6:-4]
        # use the value to get the navigation user agent used
        ua_file = open(f"C://Projects/Clickbot/uagents/ua-{randvalue}.csv", encoding='UTF8')

        # read the user agent text file
        with open(f"C://Projects/Clickbot/uagents/ua-{randvalue}.csv", encoding='utf-8-sig') as ua:
            current_agent = csv.DictReader(ua)
            browser_agent = list(current_agent)
            # print(random.choice(browser_agent))

        browser.execute_cdp_cmd("Network.setUserAgentOverride", random.choice(browser_agent))
        tz_params = {'timezoneId': random.choice(timezones)}
        # browser.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)
        rnd = random.randrange(0, 20, 1)
        link = SL.url
        browser.get(link[rnd])
        # read the cookies file
        WebDriverWait(browser, 120)
        with open(f"C://Projects/Clickbot/cookies/{file}", encoding='utf-8-sig') as cf:
            cr = csv.DictReader(cf)
            list_cookies = list(cr)
            for line in list_cookies:
                if 'secure' in line:
                    del line['secure']
                if 'expiry' in line:
                    del line['expiry']
                if 'httpOnly' in line:
                    del line['httpOnly']
                # print(line)
                browser.add_cookie(line)
        # print(filename)
        time.sleep(random.randrange(1, 20, 1))



    def mobilevisitor(self):
        WebDriverWait(browser, 120)
        res = random.choice(resolutions)
        res1 = res.split("x")
        browser.set_window_size(res[0], res[1], browser.window_handles[0])
        browser.get("https://nairobi24.co.ke")
        # print(res1[0])

    def visitotherpages(self):
        rnd = random.randrange(5, 10), 1
        browser.get("https://nairobi24.co.ke")

        elem = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[@id='menu-item-{rnd}']/a")))
        webdriver.ActionChains(browser).click(elem).perform()
        self.scrollthepage()

        elem2 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[@id='post-349']/div[1]/div/article[{rnd}]/div[2]/h4/a")))

while count < 500:
    # cycle = count / 5
    start = Clickbot()
    start.startbrowser()
    start.gotourl()
    if count % 2 != 0:
        start.scrollthepage(count)
        start.clickfirstelem(count)  # pick a random link
        start.scrollthepage(count)

    time.sleep(10)
    start.savecookies()
    start.clearcookies()
    start.restartsession()
    time.sleep(random.randrange(15, 30, 1))
    start.clearcookies()
    start.restartsession()
    time.sleep(random.randrange(0, 10, 1))
    start.scrollthepage(count)
    start.clickfirstelem(count)
    time.sleep(random.randrange(1, 10, 1))
    start.clearcookies()
    # start.retrievecookies()
    # start.scrollthepage(count)
    # start.clickfirstelem(count)
    time.sleep(random.randrange(5, 10, 1))
    count += 1
    print(count)
