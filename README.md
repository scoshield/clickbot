# Clickbot
This is a Python script that sends bot traffic to any website.

It performs automated actions such as:
1. Use different entry points, 
2. Navigate to different webpages, 
3. Automated web page scrolling
4. Change the User Agent information on every visit
5. Use a proxy server with rotating IPs and send unique IP on every request.

## Instructions

To be able to send the traffic to your website, follow the instructions
```
1. Clone the repository into your local folder
2. Download the latest Chrome Driver, rename it to chromedriver.exe and replace the existing file under /drivers folder
3. The website traffic links are in the file named socialLinks.py. This file contains shortened URL links picked from twitter. You can replace this with your social media links or shortened URLs.
4. Once you've included your links in Step 4, navigate to main.py and change this line rand_url = random.randrange(1, x, 1), x being the total number of URLs in 4.
```

