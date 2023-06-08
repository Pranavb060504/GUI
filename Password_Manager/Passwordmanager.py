from tkinter import *
import json 
from passwordgenerator import PasswordGenerator
from tkinter import messagebox

window=Tk()
window.title('Password Manager')
window.config(padx=40,pady=40)

password=PasswordGenerator()
canvas=Canvas(height=200,width=200)
logoimg=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logoimg)
canvas.grid(row=0,column=1)


#-----FUNCTIONS-------#
def save():
    website=website_textbox.get()
    email=email_textbox.get()
    password=password_textbox.get()
    empty=False


    new_data={
            website:{
                "email":email,
                "password":password
                    }
        }
    
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title='Error',message="Oops one or more blanks are empty!")
        empty=True
        website_textbox.delete(0,END)
        email_textbox.delete(0,END)
        password_textbox.delete(0,END)

    
    if not empty: 
        try:   
            with open("data.json",'r') as datafile:
                data=json.load(datafile)

        except FileNotFoundError:
                with open("data.json",'w') as datafile:
                     json.dump(new_data,datafile,indent=4)

        else:
            data.update(new_data)
            with open("data.json","w") as datafile:
                json.dump(data,datafile,indent=4)
        
        finally:
                website_textbox.delete(0,END)
                email_textbox.delete(0,END)
                password_textbox.delete(0,END)

def generate():
    password_textbox.delete(0,END)
    pas=password.generate()
    password_textbox.insert(0,f"{pas}")

def search():
    website=website_textbox.get()
    try:
        with open("data.json",'r') as datafile:
            data=json.load(datafile)
            if website in data:
                mail=data[website]['email']
                pas=data[website]['password']
                messagebox.showinfo(message=f" E-mail: {mail}\n Password: {pas}")
            else:
                 messagebox.showinfo(title='Error',message="Entry corresponding to this website does not exist")

    except FileNotFoundError:
         messagebox.showinfo(title='Error',message="File not found")
     
                         

    


#labels
website_label=Label(text='Website:')
website_label.grid(row=1,column=0)
email_label=Label(text='E-mail:')
email_label.grid(row=2,column=0)
password_label=Label(text='Password:')
password_label.grid(row=3,column=0)


#textbox
website_textbox=Entry(width=25)
website_textbox.grid(row=1,column=1)
email_textbox=Entry(width=35)
email_textbox.grid(row=2,column=1,columnspan=2)
password_textbox=Entry(width=25)
password_textbox.grid(row=3,column=1)


#buttons
search_button=Button(text='Search',command=search)
search_button.grid(row=1,column=2)
generate_password=Button(text='Generate',command=generate)
generate_password.grid(row=3,column=2)
add_button=Button(text='Add',width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()