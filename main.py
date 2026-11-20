from functions import *

while True:
    print("""

    ================================
        MINI PRODUCT SYSTEM
    ================================

    1. Bütün məhsulları göstər
    2. Qiymətə görə artan sırala
    3. Qiymətə görə azalan sırala
    4. Məhsulu adına görə axtar
    5. Məhsulu ID ilə axtar
    6. Ən ucuz məhsulu tap
    7. Ən bahalı məhsulu tap

    0. Proqramdan çıx

    ================================

    """)

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Only integers allowed")
        input("\nPress ENTER to continue...")
        continue

    if choice == str:
        print("String not allowed")
        input("\nPress ENTER to continue...")
        continue

    if choice == 1:
        showAllProducts()
        input("\nPress ENTER to continue...")

    elif choice == 2:
        sort_by_price_asc()
        input("\nPress ENTER to continue...")

    elif choice == 3:
        sort_by_price_desc()
        input("\nPress ENTER to continue...")

    elif choice == 4:
        name = input("Enter name: ")

        try:
            float(name)
            print("Numbers not allowed")
            input("\nPress ENTER to continue...")
            continue
        except ValueError:
            pass

        search_by_name(name)
        input("\nPress ENTER to continue...")

    elif choice == 5:
        id = input("Enter id: ")

        try:
            id = int(id)
        except ValueError:
            print("Only int allowed")
            input("\nPress ENTER to continue...")
            continue

        search_by_id(id)

        input("\nPress ENTER to continue...")

    elif choice == 6:
        get_cheapest_product()
        input("\nPress ENTER to continue...")

    elif choice == 7:
        get_expensive_product()
        input("\nPress ENTER to continue...")

    elif choice == 0:
        print("Closing..")
        break

    else:
        print("Something went wrong try again")
        continue