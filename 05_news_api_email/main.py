# https://newsapi.org/

import requests
import smtplib, ssl
import os
from send_email import send_email

topic = "cybersecurity OR \"cyber security\""
api_key = os.getenv("API_KEY_NEWS_EMAIL")
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&"\
      "language=en&"\
      "sortBy=publishedAt&"\
      f"apiKey={api_key}"

request = requests.get(url)
content = request.json()

message = """\
Subject: New email from NewsAPI.org

"""

for article in content["articles"][:20]:
    message = message + f"""\
Title: {article["title"]}
Description: {article["description"]}
URL: {article["url"]}

"""

message = message.encode("utf-8")
send_email(message)
