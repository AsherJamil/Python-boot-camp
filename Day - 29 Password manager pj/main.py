from tkinter import *
from tkinter import  messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def Generate_Password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 8  
    nr_symbols = 4  
    nr_numbers = 3  

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    Password_entry.delete(0, END)
    Password_entry.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = Email_Username_entry.get()
    password = Password_entry.get()
    
    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        confirmation = messagebox.askyesno(title="Confirmation", message="Are you sure about that?")
        if confirmation:
            with open("/python 100 days bootcamp/Github.git/Day - 29 Password manager pj/Save data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
    else:
        messagebox.showinfo("Error", "Please fill all fields")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo =PhotoImage(file="Day - 29 Password manager pj/logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

Email_Username_label = Label(text="Email/Username:")
Email_Username_label.grid(row=2,column=0)

Password_label=Label(text="Password:")
Password_label.grid(row=3,column=0)

website_entry = Entry(width= 39)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

Email_Username_entry = Entry(width = 39)
Email_Username_entry.grid(row=2,column=1,columnspan=2)
Email_Username_entry.insert(0,"@gmail.com")

Password_entry = Entry(width =21)
Password_entry.grid(row=3,column=1)

Generate_password_Button = Button(text="Generate Password",command=Generate_Password)
Generate_password_Button.grid(row=3,column=2)
Add_button = Button(text ="Add",width=36,command=save)
Add_button.grid(row=4, column=1,columnspan=2)

window.mainloop()



