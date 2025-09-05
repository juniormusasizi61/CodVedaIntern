import requests

# Define APIs in priority order
APIS = [
    {
        "name": "CoinGecko",
        "url": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
        "parser": lambda data: data["bitcoin"]["usd"]
    },
    {
        "name": "Binance",
        "url": "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
        "parser": lambda data: data["price"]
    },
    {
        "name": "Coindesk",
        "url": "https://api.coindesk.com/v1/bpi/currentprice.json",
        "parser": lambda data: data["bpi"]["USD"]["rate"]
    }
]

HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch_crypto_price():
    for api in APIS:
        try:
            print(f"🔎 Trying {api['name']} API...")
            response = requests.get(api["url"], headers=HEADERS, timeout=15)
            response.raise_for_status()  # check HTTP errors

            data = response.json()
            price = api["parser"](data)

            print("\n💰 Cryptocurrency Price Tracker")
            print(f"Bitcoin Price (USD): {price}")
            print(f"Source: {api['name']}")
            return

        except requests.exceptions.RequestException as e:
            print(f"⚠️ {api['name']} failed: {e}")
        except KeyError:
            print(f"⚠️ {api['name']} returned unexpected data format.")
        except Exception as e:
            print(f"⚠️ {api['name']} error: {e}")

    print("\n❌ All APIs failed. Please check your internet connection.")


if __name__ == "__main__":
    fetch_crypto_price()
