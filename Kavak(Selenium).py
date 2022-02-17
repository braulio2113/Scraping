from pandas.io.html import read_html
from selenium import webdriver
import random
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys


opts = Options()
opts.add_argument("start-maximized")
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts) 


driver.get('https://www.kavak.com/compra-de-autos')
sleep(random.uniform(2.0, 5.0))

name = 'city'

driver.find_element_by_xpath('//input[@formcontrolname="search"]').send_keys(name, Keys.ENTER)
sleep(random.uniform(1.0, 2.0))

pages = int(driver.find_element_by_xpath('//span[@class="total"]').text)

hrefs = []
for i in range(pages):
    links = driver.find_elements_by_xpath('//a[@class="card-inner"]')
    for link in links:
        href = link.get_attribute('href')
        hrefs.append(href)
    if i != pages-1:
        button = driver.find_element_by_xpath('//button[@data-cy="btn-paginator-next"]')
        button.click()
        sleep(random.uniform(1.0, 2.0))
    else:
        pass

del href
cars = []
for href in hrefs:
    driver.get(href)
    sleep(random.uniform(2.0, 5.0))
    car = pd.DataFrame()
    car['Model'] = pd.DataFrame([driver.find_element_by_xpath('//div[@class="col-lg-4"]/div/div/h1[contains(@class,"car-name ")]').text])
    car['Price'] = pd.DataFrame([driver.find_element_by_xpath('/html/body/app-root/div[2]/app-vip/main/section[1]/div/div/div[3]/div/div[2]/app-car-data/div[1]/span/strong').text])
    car['Year'] = pd.DataFrame([driver.find_element_by_xpath('/html/body/app-root/div[2]/app-vip/main/section[1]/div/div/div[3]/div/div[1]/p/span[1]').text])
    car['Mileage'] = pd.DataFrame([driver.find_element_by_xpath('/html/body/app-root/div[2]/app-vip/main/section[1]/div/div/div[3]/div/div[1]/p/span[3]').text])
    cars.append(car)
    
    
cars = pd.concat(cars)

