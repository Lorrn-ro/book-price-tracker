import requests
from bs4 import BeautifulSoup

file_name = "number.txt"

url = "https://books.toscrape.com/catalogue/sharp-objects_997/index.html"
response = requests.get(url)

# Convert raw HTML into a structured, searchable Python object
soup = BeautifulSoup(response.content, "html.parser")

price_text = soup.find("p", class_="price_color").get_text()

try:

    with open(file_name, 'r') as file:
        price = float(file.read().strip())

    if float(price_text[1:]) != price:
        print(f"PRICE CHANGED: {price} -> {float(price_text[1:])}")
        price = float(price_text[1:])
    
        with open(file_name, 'w') as file:
            file.write(str(price))
    else:
        print("No price change yet.")
except FileNotFoundError:
    print("The file doesn't exist yet! Creating it with the current price.")
    with open(file_name, 'w') as file:
            file.write(str(price_text[1:]))













