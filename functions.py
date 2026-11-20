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

def sort_by_price_asc():

    if not products:
        print("Products data empty")
        return

    products.sort(key=lambda x: x['price'])
    showAllProducts()

def sort_by_price_desc():
    if not products:
        print("Products data empty")
        return
    
    products.sort(key=lambda x: x['price'], reverse=True)
    showAllProducts()

def search_by_name(name):

    if not products:
        print("Products data empty")
        return

    for x in products:
        if x['name'].lower() == name.lower():
            print(f"ID: {x['id']}")
            print(f"Name: {x['name']}")
            print(f"Price: {x['price']}")
            print("-" * 30)
            return

    print("Product not found")

def search_by_id(id):

    if not products:
        print("Products data empty")
        return

    for x in products:
        if x['id'] == id:
            print(f"ID: {x['id']}")
            print(f"Name: {x['name']}")
            print(f"Price: {x['price']}")
            print("-" * 30)
            return

    print("Product not found")

def get_cheapest_product():

    if not products:
        print("Products data empty")
        return

    cheapest = min(products, key=lambda x: x['price'])

    print(f"ID: {cheapest['id']}")
    print(f"Name: {cheapest['name']}")
    print(f"Price: {cheapest['price']}")
    print("-" * 30)

def get_expensive_product():

    if not products:
        print("Products data empty")
        return

    expensive = min(products, key=lambda x: x['price'])

    print(f"ID: {expensive['id']}")
    print(f"Name: {expensive['name']}")
    print(f"Price: {expensive['price']}")
    print("-" * 30)


