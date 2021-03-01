from tkinter import * #only imports classes
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_let = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_nr = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_sy = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_let + password_nr + password_sy
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()
    print(type(password_data))

    if len(website_data)==0 or len(email_data)==0 or len(password_data) == 0:
        messagebox.showinfo(title="oops", message="Please fill out all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message= f'These are the details: \n Email:{email_data}\n Password:{password_data}\n Save?')
        if is_ok:
            with open("my_info.txt", mode="a") as my_info:
                my_info.write(f"Website:{website_data}, Email:{email_data}, Password:{password_data}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady = 50)

canvas = Canvas(width=200,height=200, highlightthickness= 0)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image =password_logo)
canvas.grid(column=2,row=1)

website_label= Label(text = "Website:")
website_label.grid(column=1, row=2)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column = 2, row = 2, columnspan=2)

email_label= Label(text = "Email/Username:")
email_label.grid(column=1, row=3)

email_input = Entry(width=35)
email_input.grid(column = 2, row = 3, columnspan=2)

password_label= Label(text = "Password:")
password_label.grid(column=1, row=4)

password_input = Entry(width=21)
password_input.grid(column = 2, row = 4)

password_button = Button(text = "Generate Password", highlightthickness=2, command = generate_password)
password_button.grid(column =3, row =4)

add_button = Button(window, text = "Add", highlightthickness=0, width = 36, command = save_password, highlightbackground = '#dddddd')
add_button.grid(column =2, row =5, columnspan =2 )

window.mainloop()