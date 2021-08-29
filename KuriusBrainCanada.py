from tkinter import *
from tkinter import filedialog
import os

def delete1():
  screen1.destroy()

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("420x420")
  screen3['bg']='#FF1212'
  Label(screen3,image=photo).pack()
  Label(screen3,text = "Name of the Project", bg = "#3B48C3", width = "300", height = "2", font = ("Times New Roman", 13,'bold')).pack()
  Label(screen3,text="",bg="#FF1212").pack()

  Button(screen3, text="Choose the Excel",width='30',height='2').pack()
  Label(screen3,text="",bg="#FF1212").pack()

  Button(screen3, text="Execute the Programme",width='30',height='2').pack()
  Label(screen3,text="",bg="#FF1212").pack()
  Label(screen3,text = "The Output", bg = "grey", width = "300", height = "2", font = ("Times New Roman", 13,'bold')).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("420x420")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("420x420")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    
    if password1 == verify[1]:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  

  Label(screen1, image =photo).pack()
  screen1.geometry('420x500')
  screen1['bg'] = '#FF1212'

  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
  Label(screen1,text = "",bg = "#FF1212").pack()
  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "", bg='#FF1212').pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1,text = "",bg = "#FF1212").pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1,text = "",bg = "#FF1212").pack()
  Button(screen1, text = "Register", width = 30, height = 2, command = register_user).pack()
  Label(screen1,text = "",bg = "#FF1212").pack()
  Button(screen1, text = "Go Back to the Main Page", width = 30, height = 2, command = delete1).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  Label(screen2, image = photo).pack()
  screen2.geometry("420x500")
  screen2['bg']='#FF1212'
  Label(screen2,text = "Name of the Project", bg = "#3B48C3", width = "300", height = "2", font = ("Times New Roman", 13,'bold')).pack()
  Label(screen2,text = "",bg = "#FF1212").pack()
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2,text = "",bg = "#FF1212").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2,text = "",bg = "#FF1212").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2,text = "",bg = "#FF1212").pack()
  Button(screen2, text = "Login", width ='30', height = '2', command = lambda:[login_verify(),screen2.destroy()]).pack()
  Label(screen2,text = "",bg = "#FF1212").pack()
  Button(screen2, text = "Back to Main Page", width ='30', height = '2', command = lambda:[screen2.destroy()]).pack()
  
  
def main_screen():
  global screen
  global photo
  screen = Tk()
  photo = PhotoImage(file = "download.png")
  labelphoto = Label(screen, image =photo)
  labelphoto.pack()
  screen.geometry('420x420')
  screen.title("MAIN PAGE")
  screen['bg'] = '#FF1212'
  Label(text = "Name of the Project", bg = "#3B48C3", width = "300", height = "2", font = ("Times New Roman", 13,'bold')).pack()
  Label(text = "",bg = "#FF1212").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "",bg = "#FF1212").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()
  Label(text = "",bg = "#FF1212").pack()


  screen.mainloop()

main_screen()
  
