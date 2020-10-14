import requests
import re
from bs4 import BeautifulSoup
import time
import selenium
import matplotlib.pyplot as plt
from selenium.common.exceptions import NoSuchElementException        
from selenium.common.exceptions import StaleElementReferenceException  
from datetime import datetime      
from urllib.parse import urlencode
from constants import Constant
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

price_list_total = 0
manufacturer_list_total = []
model_list_total = []
mileage_list_total = []
year_manufactured_list_total = []
datetime_list_total = []

def get_scraped_results(params):

    # Set headers
    headers = requests.utils.default_headers()
    headers.update(
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    url = 'https://www.sauto.cz/osobni/hledani#!' + urlencode(params, doseq=True)

    options = Options()
    options.headless = False
    driver = webdriver.Chrome(chrome_options=options)

    def render_page(url):
        driver.get(url)
        time.sleep(3)
        r = driver.page_source
        return r

    def return_int(value):
        return int(value.replace(" ", ""))

    def get_date_time():
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    r = render_page(url)

    soup = BeautifulSoup(r, "html.parser")

    average = 0
    value = ""
    price = 0
    sum_total = 0
    items_total = 0

    def scrape():
        sum = 0
        items = 0
        price_list = []
        manufacturer_list = []
        model_list = []
        mileage_list = []
        year_manufactured_list = []
        datetime_list = []
        for i in soup.select('.price strong:not(#pvContent .price strong)'):
            sum += return_int(i.text)
            manufacturer = driver.find_elements_by_css_selector(".carBoxContent h1")[0].text
            manufacturer_list.insert(items, manufacturer)
            model = driver.find_element_by_css_selector(".modelBox h1").text
            model_list.insert(items, model)
            yearManufactured = driver.find_elements_by_css_selector(".content dl")[items].find_elements_by_css_selector("dd")[1].text
            year_manufactured_list.insert(items, return_int(yearManufactured))
            mileage = driver.find_elements_by_css_selector(".content dl")[items].find_elements_by_css_selector("dd")[2].text
            mileage_list.insert(items, return_int(re.sub("[^\\d]", "", mileage)))
            datetime = get_date_time()
            datetime_list.insert(items, datetime)
            price_list.insert(items, return_int(i.text))
            items += 1
        result = (sum, items, price_list, manufacturer_list, model_list, mileage_list, year_manufactured_list, datetime_list)     
        return result

    tuple = scrape()
    sum_total = tuple[0]
    items_total = tuple[1]
    price_list_total = tuple[2]
    manufacturer_list_total = tuple[3]
    model_list_total = tuple[4]
    mileage_list_total = tuple[5]
    year_manufactured_list_total = tuple[6]
    datetime_list_total = tuple[7]

    def check_exists_by_cssSelector(css):
        try:
            driver.find_element_by_css_selector(css)
        except NoSuchElementException:
            return False
        except StaleElementReferenceException:
            return False
        return True

    element_string = "#nextPage"

    while check_exists_by_cssSelector(element_string):
        driver.find_element_by_css_selector(element_string).click()
        time.sleep(3)
        r = render_page(driver.current_url)
        soup = BeautifulSoup(r, "html.parser")
        tuple = scrape()
        sum_total += tuple[0]
        items_total += tuple[1]
        price_list_total += tuple[2]
        manufacturer_list_total += tuple[3]
        model_list_total += tuple[4]
        mileage_list_total += tuple[5]
        year_manufactured_list_total += tuple[6]
        datetime_list_total += tuple[7]

    driver.quit()

    average = sum_total / items_total

    print("Items: " + str(items_total))
    print("Min: " + str(min(price_list_total)))
    print("Max: " + str(max(price_list_total)))
    print("Average: " + str(average))

    return (manufacturer_list_total, model_list_total, price_list_total, mileage_list_total, year_manufactured_list_total, datetime_list_total) 