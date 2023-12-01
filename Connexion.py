from customtkinter import *
import pymysql
import User_class as user_file
from tkinter import messagebox
import Database as Db

def Show_Account(Frame):
    Frame.destroy()
    from Compte import Create_Frame_Compte
    Create_Frame_Compte()
    
def Delete_User():
    FileUser = open("Connect_User.txt", "w")
    FileUser.close()    

def Show_New_User(Frame):
    Frame.destroy()
    from newAccountUser import Create_New_Account_Frame
    Create_New_Account_Frame()
    
def Reset_Loading():
    FileLoad = open("Loading.txt", "w")
    FileLoad.write("0")
    FileLoad.close()

def verif_input_connec(mail, password, frame):
    error=0
    indication=""
    MailExist = Db.Query("SELECT COUNT(*) FROM User WHERE mail = '"+ str(mail) +"'; ")
    MailExist = Db.formatage(MailExist)
    print(MailExist)
    PasswordCorrect = Db.Query("SELECT COUNT(*) FROM User WHERE mail = '"+ str(mail) +"' AND password = '"+ str(password) +"';")
    PasswordCorrect = Db.formatage(PasswordCorrect)
    print(PasswordCorrect)
    if mail=="":
        error+=1
        indication="Mail Adress"
    elif MailExist[0]==0:
        error+=1
        indication="This mail adress doesn't exist."
    elif password=="":
        error+=1
        indication="Password"
    elif PasswordCorrect[0]==0:
        error+=1
        indication="The password is not correct."
        
    if error==0:
        ID_Connection = Db.Query("SELECT ID_User FROM User WHERE mail='"+ str(mail) +"' AND password='"+ str(password) +"';")
        ID_Connection = Db.formatage(ID_Connection)
        if len(ID_Connection)>0:
            print("Connected as "+str(ID_Connection[0]))
            FileUser = open("Connect_User.txt", "w")
            FileUser.write(str(ID_Connection[0]))
            FileUser.close()
            Show_Account(frame)
        else:
            print("Error, your account doesn't exist.")
            messagebox.showinfo("error", "Error, your account doesn't exist.")
    else:
        messagebox.showinfo("error", "ERROR INPUTS: "+ str(indication))
    

def Create_Connection_Frame():

    Frame = CTk()
    Frame.title("Skyblitz")
    Frame.geometry("1920x1080")

    Frame.grid_columnconfigure(0, weight=3)
    Frame.grid_columnconfigure(1, weight=1)
    Frame.grid_columnconfigure(2, weight=3)

    Frame.grid_rowconfigure(0, weight=3)
    Frame.grid_rowconfigure(1, weight=1)
    Frame.grid_rowconfigure(2, weight=3)

    set_appearance_mode('light')

    Div = CTkFrame(master=Frame, fg_color="#CBCBCB", corner_radius=25)
    Div.grid(row=1, column=1, sticky="nsew")

    Div.grid_columnconfigure(0, weight=1)

    Div.grid_rowconfigure(0, weight=1)
    Div.grid_rowconfigure(1, weight=1)
    Div.grid_rowconfigure(2, weight=1)
    Div.grid_rowconfigure(3, weight=1)

    # ------------------------- Title 
    Title_Label = CTkLabel(
        master=Div, 
        width=200, 
        height=50,
        text="CONNECTION",
        text_color="#000000",
        font=("Arial", 40, "bold"),
        corner_radius=10
        )
    Title_Label.grid(row=0, column=0, pady=(10, 0))

    #--------------------------- Email

    email_entry = CTkEntry(
        master=Div, 
        fg_color="#DBDBDB",
        text_color="#000000",
        font=("Arial", 22, "bold"),
        width=200, 
        height=50,
        placeholder_text="E-mail"
        )
    email_entry.grid(row = 2, column = 0, pady=(20, 10))

    #--------------------------- Password

    password_entry = CTkEntry(
        master=Div, 
        fg_color="#DBDBDB",
        text_color="#000000",
        font=("Arial", 22, "bold"),
        width=200, 
        height=50,
        placeholder_text="Password"
        )
    password_entry.grid(row = 4, column = 0, pady=(10, 20))
    password_entry.configure(show='*')

    #--------------------------- Buttons
    button_createAccount = CTkButton(Div, 
                                    text="Create a new account", 
                                    command=lambda: Show_New_User(Frame), 
                                    width=200, height=50, 
                                    font=("Arial", 20, "underline"), 
                                    fg_color="transparent", text_color="#FF764A",
                                    corner_radius=50)
    button_createAccount.grid(row = 6, column = 0, pady=20)

    button_connect = CTkButton(Div, 
                                    text="Connect", 
                                    command=lambda: verif_input_connec(email_entry.get(), password_entry.get(), Frame), 
                                    width=200, height=50, 
                                    font=("Arial", 20, "bold"), 
                                    fg_color="#FF764A", text_color="#000000", hover_color="#FF4C13",
                                    corner_radius=50,
                                    )
    button_connect.grid(row = 5, column = 0, pady=20)
    
    def on_closing():
        Delete_User()
        Reset_Loading()
        print("Fermeture de la page.")
        Frame.destroy()
    
    Frame.protocol("WM_DELETE_WINDOW", on_closing)

    Frame.mainloop()