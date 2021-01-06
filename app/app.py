import ast
from slack_notification import send_slack_notification
from scrape_zoopla import get_property_page, get_price_estimate_from_page, get_address_from_page
from configparser import ConfigParser
import schedule
import time


def job():
    config = ConfigParser()
    config.read('config.ini')
    urls = ast.literal_eval(config.get('main', 'urls'))
    webhook_url = config.get('main', 'slack_webhook_url')
    for url in urls:
        property_page = get_property_page(url)
        price_estimate = get_price_estimate_from_page(property_page)
        address = get_address_from_page(property_page)
        entry = f"Address: {address} - Price Estimate: £{price_estimate}"
        send_slack_notification(webhook_url, entry)


if __name__ == "__main__":

    schedule.every().day.at("09:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(50)
