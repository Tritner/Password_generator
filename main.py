FONT = "Arial"
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def save():
    Website = Website_entry.get()
    username = Username_entry.get()
    password = Password_entry.get()
    new_data = {
        Website :{
            "username" : username,
            "password" : password
        }
    }
    if len(Website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Something wrong",message="do not leave empty fields")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)

        finally:
            Website_entry.delete(0, END)
            Password_entry.delete(0, END)

def search():
    website = Website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Something wrong", message="dont have file with passwords yet!")
    if website in data:
        messagebox.showinfo(title="your username and password", message=f"Username: {data[website]["username"]}\nPassword: {data[website]["password"]}")
    else:
        messagebox.showerror(title="Something wrong", message="you dont have password for this website")


def generate():
    Password_entry.delete(0, END)
    #generate random strong password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    #in case user wants to use the password that genarated
    pyperclip.copy(password)
    Password_entry.insert(0, password)


#init window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
#init canvas
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.grid(column=1,row=0)
#use logo
Lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=Lock_img)

Website_label = Label(text="Website:")
Website_label.grid(column=0,row=1)
Website_entry = Entry(width=34)
Website_entry.focus()
Website_entry.grid(column=1,row=1,columnspan=2,sticky="w")

Username_label = Label(text="Email/Username:")
Username_label.grid(column=0,row=2)
Username_entry = Entry(width=52)
Username_entry.insert(0,"example@gmail.com")
Username_entry.grid(column=1,row=2,columnspan=2)

Password_label = Label(text="Password:")
Password_label.grid(column=0,row=3)
Password_entry = Entry(width=33)
Password_entry.grid(column=1,row=3,columnspan=2,sticky="w")

add_button = Button(text="Add",width=44,command=save)
add_button.grid(column=1,row=4,columnspan=2)

generate_button = Button(text="Generate  password",command=generate)
generate_button.grid(column=2,row=3,columnspan=2,sticky="w")

search_button = Button(text="Search    password ",command=search)
search_button.grid(column=2,row=1,columnspan=1)

window.mainloop()

