# admin.py file
from menu import Menu

class Admin:
    def add_Menu(self):
        try:
            id = int(input("Enter menu id:"))
            name = input("Enter name:")
            price = int(input("Enter price:"))
            quantity = int(input("Enter quantity:"))
            m = Menu(id, name, price, quantity)

            with open("menu.txt", "a") as fp:
                fp.write(str(m) + "\n")

            print("Menu added successfully!")
        except ValueError:
            print("Invalid input. Please enter valid numerical values for price and quantity.")


    def display_Menu(self):
        try:
            with open("menu.txt", "r") as fp:
               for m in fp:
                    sep_txt = m.split(',')
                    print("id:", sep_txt[0])
                    print("name:",sep_txt[1])
                    print("price:", sep_txt[2])
                    print("quantity:", sep_txt[3])
        except FileNotFoundError:
            print("Error: menu file not found")
        except Exception as e:
            print(f"Error: {e}")


    def search_Menu(self, Menu_id):
        with open("menu.txt", "r") as fp:
            for m in fp:
                try:
                    m.index(str(Menu_id), 0, 4)
                    print("Menu Found")
                    break
                except ValueError:
                    pass
            else:
                print("Menu not Found")

    def delete_Menu(self, Menu_id):
        container = []
        found = False
        try:
            with open("menu.txt", "r") as fp:
               for m in fp:
                   sep_list = m.split(",")
                   if sep_list[0] == str(Menu_id):
                     found = True
                   else:
                     container.append(m)

            if found:
                with open("menu.txt", "w") as fp:
                    for x in container:
                      fp.write(x)
                print("Menu deleted successfully!")
            else:
               print("Menu not found. Deletion failed.")
        except FileNotFoundError:
            print("Error: menu file not found")
        except Exception as e:
            print(f"Error: {e}")

    def update_Menu(self, Menu_id):
        container = []
        found = False
        try:
            with open("menu.txt", "r") as fp:
                for m in fp:
                    sep_list = m.split(",")
                    if sep_list[0] == str(Menu_id):
                       found = True
                       ans = input("Do you want to change name: (y/n)")
                       if ans == 'y':
                         sep_list[1] = input("Enter new name:")
                       ans = input("Do you want to change price: (y/n)")
                       if ans == 'y':
                         sep_list[2] = input("Enter new price:")

                       m = ','.join(sep_list)
                       print("Menu updated successfully!")

                    container.append(m)
                if found:
                    with open("menu.txt", 'w') as fp:
                      for x in container:
                       fp.write(x)
                else:
                  print("Id not present")
        except FileNotFoundError:
            print("Error: menu file not found")
        except Exception as e:
            print(f"Error: {e}")
