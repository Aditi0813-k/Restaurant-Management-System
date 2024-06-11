# user.py file
class User:
    def search_Menu(self, Menu_id):
        try:
            with open("menu.txt", "r") as file:
                for m in file:
                    menu_data = m.split(',')
                    if menu_data[0] == str(Menu_id):
                        print("Menu Found")
                        print(m)
                        break
                else:
                    print("Menu Not Found")

        except FileNotFoundError:
            print("Error: File Not found")

    def display_Menu(self):
        try:
            with open("menu.txt", "r") as file:
                lines = file.readlines()

            if not lines:
                print("No menu found in the file.")
                return
            
            for m in lines:
                menu_data = [item.strip() for item in m.split(',')]
                if len(menu_data) >= 4:
                    print("Id: ", menu_data[0])
                    print("Name: ", menu_data[1])
                    print("Price: ", menu_data[2])
                    print("Quantity: ", menu_data[3])
                else:
                    print("Invalid menu format")
        except FileNotFoundError:
            print("Error: menu file not found")
        except Exception as e:
            print(f"Error: {e}")

    def place_order(self, menu_id, quantity):
        try:
            menus = []
            menu_found = False
            order_details = []

            with open("menu.txt", "r") as fp:
                for m in fp:
                    menu_data = m.split(',')
                    if len(menu_data) >= 4 and menu_data[0] == str(menu_id):
                        menu_name = menu_data[1]
                        menu_price = int(menu_data[2])
                        remaining_quantity = int(menu_data[3]) - quantity

                        if remaining_quantity < 0:
                            print("Insufficient Stock...")
                            return

                        order_cost = menu_price * quantity

                        order_details.append(f"Product: {menu_name}")
                        order_details.append(f"Quantity: {quantity}")
                        order_details.append(f"Cost: {order_cost}")

                        updated_menu = f"{menu_data[0]},{menu_name},{menu_price},{remaining_quantity}"
                        menus.append(updated_menu)

                        menu_found = True
                    else:
                        menus.append(m.strip())

            if not menu_found:
                print("Error: Menu ID not found.")
                return

            with open("menu.txt", "w") as file:
                for e in menus:
                    file.write(e + "\n")

            with open("order.txt", "a") as order_file:
                order_file.write("\n" + "\n".join(order_details) + "\n")

            print("Order Placed Successfully..")
        except FileNotFoundError:
            print("Error: menu file not found")
        except Exception as e:
            print(f"Error occurred: {e}")

    def pay_bill(self):
        try:
            total_bill = 0
            order_details = []

            with open("order.txt", "r") as order_file:
                for e in order_file:
                    if 'Cost:' in e:
                        cost = int(e.strip().split(':')[1].strip())
                        total_bill += cost
                    elif e.strip():
                        order_details.append(e.strip())

            if not order_details:
                print("Error: No product details found. Please place an order.")
                return

            print("Order Details:")
            for details in order_details:
                print(details, end=" \n")
            print("\nTotal Bill : ", total_bill)

    
            with open("order.txt", "w") as order_file:
                pass

        except FileNotFoundError:
            print("Error: Order file not found")
        except Exception as e:
            print(f"Error occurred: {e}")

