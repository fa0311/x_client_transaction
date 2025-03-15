
import requests

from x_client_transaction.transaction import ClientTransaction

twitter_key = requests.get("https://raw.githubusercontent.com/fa0311/TwitterInternalAPIDocument/refs/heads/master/docs/json/Translation.json").json()
latest_user_agent = requests.get("https://raw.githubusercontent.com/fa0311/latest-user-agent/refs/heads/main/header.json").json()
chrome = latest_user_agent["chrome"]

chrome.pop("host")
chrome.pop("connection")

home_page_response = requests.get("https://x.com/", headers=chrome).text


transaction  = ClientTransaction(home_page_response, twitter_key["index"][0], twitter_key["index"][1:])

data = transaction.generate_transaction_id("GET", "/api/v1/transactions")
print(data)
print(ClientTransaction.decode_transaction_id(data))

