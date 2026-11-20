import json

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

def showAllProducts():

    if not products:
        print("Products data empty")
        return

    for x in products:
        print(f"ID: {x['id']}")
        print(f"Name: {x['name']}")
        print(f"Price: {x['price']}")
        print("-" *30)
