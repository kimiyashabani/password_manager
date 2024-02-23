import tkinter.messagebox
from tkinter import *
import pyperclip
from random import shuffle, randint, choice
import json

# TODO : 1- UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(window, width=200, height=200)

# photo:
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# labels:
website_label = Label(window, text="Website:")
username_label = Label(window, text="Username/Email:")
password_label = Label(window, text="Password:")
website_label.grid(row=1, column=0, pady=5)
username_label.grid(row=2, column=0, pady=5)
password_label.grid(row=3, column=0, pady=5)

# entries:
website_entry = Entry(width=32)
website_entry.focus()
username_entry = Entry(width=50)
password_entry = Entry(width=32)
website_entry.grid(row=1, column=1,)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)


# TODO : 2- RANDOM PASSWORD GENERATOR FUNCTION
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(1, 8))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password = random_letters + random_numbers + random_symbols
    shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# TODO : 3- SAVE PASSWORD
def add_to_passwords():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        tkinter.messagebox.showerror("Error", "All files are required")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website,
                                               message=f"These are the details entered: \nEmail: {username} "
                                                       f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            new_password = {
                website: {
                    "username": username,
                    "password": password
                }
            }
            with open("passwords.json", "w") as passwords:
                json.dump(new_password, passwords, indent= 4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
def calling_search_website():
    website_name = website_entry.get()
    search_website(website_name)
def search_website(website_name):
    with open("passwords.json", "r") as passwords:
        passwords_data = json.load(passwords)
        try:
            data = passwords_data[website_name]
            tkinter.messagebox.showinfo("Website found", message=f"username: {data['username']}\npassword: {data['password']}")
        except:
            tkinter.messagebox.showerror("website not found", message="You do not have an account in this website")

# buttons:
load_button = Button(text="Search", command=calling_search_website, width=14)
generate_password_button = Button(text="Generate password", command=generate_password, width=14)
add_button = Button(text="Add", width=40, command=add_to_passwords)
load_button.grid(row=1, column=2 , columnspan=2)
generate_password_button.grid(row=3, column=2)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
