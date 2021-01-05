import requests

def send_slack_notification(webhook_url, house_price):
    response = requests.post(webhook_url, json={"text":house_price})
