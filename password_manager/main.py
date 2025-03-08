from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT = ("arial", 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(8, 10))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter + symbol + number
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_text.get()
    user = user_text.get()
    passcode = password_text.get()

    if len(site) == 0 or len(passcode) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \nUser/Email: {user}"
                                                           f"\nPassword: {passcode} \n Is it OK to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{site} | {user} | {passcode} \n")
                site_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
site_label = Label(text="Website:", font=FONT)
site_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:", font=FONT)
user_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# Text Entries
site_text = Entry(width=35)
site_text.focus()
site_text.grid(row=1, column=1, columnspan=2)

user_text = Entry(width=35)
user_text.insert(0, "test@email.com")
user_text.grid(row=2, column=1, columnspan=2)

password_text = Entry(width=21)
password_text.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", font=FONT, width=14, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=FONT, width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
