from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# create save function to save inputs into an external file
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
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
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()