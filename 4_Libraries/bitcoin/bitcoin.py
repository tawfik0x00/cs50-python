import sys
import requests


if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])

    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey").json()
    amount = float(response["data"]["priceUsd"]) * value
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("An Problem occured!")
    sys.exit(1)

