from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # create lists with list comprehension to save random letters, symbols, numbers with given random range
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # add all lists to create one list
    password_list = password_letters + password_symbols + password_numbers

    # shuffle element positions
    shuffle(password_list)

    # combine elements to create a string
    password = "".join(password_list)
    password_entry.insert(0, password)
    # copy password when generated to make it paste ready
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# create save function to save inputs into an external file
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # check if user leaves website & password fields empty and show a warning message
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        # show a message box to ask user if inputs are enough or not
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email}"
                                                                f"\nPassword: {password} \nIs it ok to save?")
        # if user answers positive to message box, append inputs to txt and empty input fields
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas & show an image in it
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# create labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# create entries
website_entry = Entry(width=54)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@example.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# create buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()