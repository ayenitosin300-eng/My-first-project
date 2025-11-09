# account_ui.py
import json
import os

DB_FILE = "accounts.json"

# Load existing accounts
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        accounts = json.load(f)
else:
    accounts = {}

def save_accounts():
    with open(DB_FILE, "w") as f:
        json.dump(accounts, f, indent=2)

def create_account():
    username = input("Enter new username: ")
    if username in accounts:
        print("User already exists!")
        return
    password = input("Enter password: ")
    accounts[username] = {"password": password}
    save_accounts()
    print(f"Account '{username}' created.")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if accounts.get(username, {}).get("password") == password:
        print(f"Welcome {username}!")
    else:
        print("Invalid credentials.")

def main_menu():
    while True:
        print("\n1. Create Account\n2. Login\n3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
