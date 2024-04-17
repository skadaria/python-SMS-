#This is entry point of the application
from Utils import login, register_user, admin_dashboard, student_dashboard
def main():
    while True:
        print("*************************************")
        print("|     EDUCATION PROFILE SYSTEM       |")
        print("*************************************")
        print("|         1. Login                   |")
        print("|         2. Register                |")
        print("|         3. Exit                    |")
        print("--------------------------------------")

        choice = input("\nEnter your choice(1/2/3): ")

        if choice == '1':
            user = login()
            if user:
                if user.role == "admin":
                    admin_dashboard(user)
                else:
                    student_dashboard(user)
            else:
                print("Login failed.") 
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("\nExiting the program Good bye!!")
            break  # Exit the program
        else:
            print("Invalid choice.") 

if __name__ == "__main__":
    main()