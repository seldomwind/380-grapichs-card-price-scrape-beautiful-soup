from bs4 import BeautifulSoup
import requests
url='https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4472105&quicklink=true'

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print("Nividia Geforce RTX 380 Graphics Card current price: ", strong.string)