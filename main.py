# main.py file
from admin import Admin
from user import User

def admin_login():
    admin_email = input("Enter Email: ")
    admin_password = input("Enter Password: ")

    if admin_email == "r@gmail.com" and admin_password == "123":
        return True
    else:
        print("Invalid Email and password")
        return False
    
def user_login():
    user_email = input("Enter User Email: ")
    user_password = input("Enter User Password: ")
    if user_email == "user@gmail.com" and user_password == "123":
        return True
    else:
        print("Invalid email or password.")
        return False


if __name__ == "__main__":
    admin_obj = Admin()  
    user_obj = User()

    while True:
        print()
        print("***Restaurant Management System***")
        print("""
              1. Admin
              2. User
              3. Exit""")
        try:
            ch = int(input("Enter your Choice: "))

            if ch == 1:
                print("******************Please Login to your Account***************")
                if admin_login():
                    admin_ch = 0 
                    while admin_ch != 6:
                        print()
                        print("** ADMIN MENU LIST **")
                        print("""
                                Admin Menu
                                1. Add Menu
                                2. Display Menu
                                3. Update Menu
                                4. Delete Menu
                                5. Search Menu
                                6. Exit
                                    """) 
                        
                        try:
                            admin_ch = int(input("Enter your choice: "))
                            if admin_ch == 1:
                                admin_obj.add_Menu()  # Fix function name
                            elif admin_ch == 2:
                                admin_obj.display_Menu()  # Fix function name
                            elif admin_ch == 3:
                                Menu_id = int(input("Enter Menu ID to update: "))
                                admin_obj.update_Menu(Menu_id)  # Fix function name
                            elif admin_ch == 4:
                                Menu_id = int(input("Enter the Menu id you want to delete: "))
                                admin_obj.delete_Menu(Menu_id)  # Fix function name
                            elif admin_ch == 5:
                                Menu_id = int(input("Enter Menu ID to search: "))
                                admin_obj.search_Menu(Menu_id)  # Fix function name
                            elif admin_ch == 6:
                                print("Exiting Admin......")
                            else:
                                print("Invalid Choice.. Please enter a valid number")
                        except ValueError:
                            print("Invalid Input.. Please enter a valid number")

            elif ch == 2:
                print("******************Please Login to your Account***************")
                if user_login():
                    user_ch = 0
                    while user_ch != 5:
                        print()
                        print("** USER MENU LIST **")
                        print("""
                                User Menu:
                                1. Search Menu
                                2. Display Menu
                                3. Place Order
                                4. Pay Bill
                                5. Exit
                                    """)
                        try:
                            user_ch = int(input("Enter Your Option: "))
                            if user_ch == 1:
                                Menu_id = int(input("Enter Menu ID to search: "))
                                user_obj.search_Menu(Menu_id)
                            elif user_ch == 2:
                                user_obj.display_Menu()
                            elif user_ch == 3:
                                Menu_id = int(input("Enter Menu ID to order: "))
                                quantity = int(input("Enter quantity: "))
                                user_obj.place_order(Menu_id, quantity)
                            elif user_ch == 4:
                                user_obj.pay_bill()
                            elif user_ch == 5:
                                print("Exiting User Menu...")
                                break
                            else:
                                print("Invalid Choice.. Please enter a valid number")
                        except ValueError:
                            print("Invalid Input.. Please enter a valid number")

            elif ch == 3:
                print("Exiting....")
                break
                
            else:
                print("Invalid Choice.. Please Enter (1-3)")

        except ValueError:
            print("Invalid Input.. Please enter a valid number")
