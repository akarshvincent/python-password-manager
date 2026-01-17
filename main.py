from tkinter import *
from tkinter import messagebox
from passwordGen import generate_password
import pyperclip
import json

def handle_search():
    website = entry_web.get().strip().lower()
    with open("data.json" , "r") as data_file:
        data = json.load(data_file)
        for key in data:
            if key.lower() == website:
                email = data[key]["email"]
                passwd = data[key]["password"]
                pyperclip.copy(passwd)
                messagebox.showinfo(title=website.capitalize(), message=f"Your Username/Email: {email} \n\nYour Password: {passwd}")
                return

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

def handle_generate():
    password = generate_password()
    entry_pass.delete(0 , END)
    entry_pass.insert(0, password)
    pyperclip.copy(password)

def save():
    website = entry_web.get()
    email = entry_user.get()
    passwd = entry_pass.get()
    new_data = {
        website:{
        "email" : email,
        "password" : passwd
     },
    }

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showerror(title= "Warning", message= "Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Details entered: \n Email/Username: {email} \n Password: {passwd} \n Is it okay to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data , data_file, indent =4)

            else:
                data.update(new_data)
                messagebox.showinfo(title="Done", message="Saved Successfully")
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_web.delete(0, END)
                entry_pass.delete(0, END)


window = Tk()
window.title("Password Manager")
window.iconbitmap("ico.ico")

window.config(padx=50 , pady=50)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

canvas = Canvas(width = 200 , height= 200)
logo_img = PhotoImage(file = "logo2.png")

canvas.create_image(100, 100 , image = logo_img)
canvas.grid(column = 1, row = 0 )

label1 = Label(text= "Website:")
label1.grid(column= 0, row =  1 )

label2 = Label(text= "Email/Username:")
label2.grid(column= 0, row =  2 )

label3 = Label(text= "Password:")
label3.grid(column= 0, row =  3 )


entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, sticky="ew", padx=(0, 5))
entry_web.focus()

entry_user = Entry(width=35)
entry_user.grid(column=1, row=2, columnspan=2, sticky="ew")
entry_user.insert(0, "akarshvincent@gmail.com")

entry_pass = Entry()
entry_pass.grid(column=1, row=3, sticky="ew", padx=(0, 5))


button = Button(text="Generate Password" ,command = handle_generate)
button.grid(column=2, row=3, sticky="w")

button = Button(text="Add", width=30, command= save)
button.grid(column=1, row=4, columnspan=2, sticky="ew")

button = Button(text = "Search", command= handle_search)
button.grid(column=2, row=1, sticky="ew")


window.mainloop()
