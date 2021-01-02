import requests
import re
from bs4 import BeautifulSoup
from configparser import ConfigParser
import ast

def get_property_page(url):
    page = requests.get(url)
    if page.status_code == 200:
        return page.content
    else:
        raise ValueError("Could not find property page")


def get_price_estimate_from_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    estimates = soup.findAll("p", {"class", "pdp-estimate__price"})
    for estimate in estimates:        
        if "pcm" in estimate.string:
            print("rental")
        else:
            return get_value_from_price_estimate_string(estimate.string)


def get_address_from_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup.h1.string


def get_value_from_price_estimate_string(string):
    intermediate_string = re.sub('[k]', '000', string)
    return re.sub('[^0-9]', '', intermediate_string)    


if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')
    urls = ast.literal_eval(config.get('main', 'urls'))
    for url in urls:
        property_page = get_property_page(url)
        price_estimate = get_price_estimate_from_page(property_page)
        address = get_address_from_page(property_page)
        print(f"Address: {address} - Price Estimate: {price_estimate}")
    