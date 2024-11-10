from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# API endpoint URLs
BITCOIN_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
ETHEREUM_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'

def fetch_price(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error("Error fetching data", exc_info=e)
        return {"error": "Failed to fetch data"}

@app.route('/bitcoin', methods=['GET'])
def bitcoin_price():
    return jsonify(fetch_price(BITCOIN_API_URL))

@app.route('/ethereum', methods=['GET'])
def ethereum_price():
    return jsonify(fetch_price(ETHEREUM_API_URL))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
