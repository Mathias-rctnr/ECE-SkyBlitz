from customtkinter import *
import pymysql
import User_class as user_file
from tkinter import messagebox

# mysqlconnect: Function connecting with the database
# Input : NO
# Output : NO
def mysqlconnect():
    conn = pymysql.connect(
    host='localhost',
    user='root',
    db='bdd_skyblitz',
    port=8080 #3306
    )
    return conn

# db_close_connection: Function deconnecting with the database
# Input : conn
# Output : NO
def db_close_connecction(conn):
    conn.close()


def update(query):
    try:
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        db_close_connecction(conn)
        print("Mise à jour réussie.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")


# Sql_Query: Function that returns the requested query
# Input : conn, query
# Output : output
def Sql_Query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    output = cur.fetchall()
    return output

# Query: Function gathering connecting, requesting and deconnecting from the database
# Input : query
# Output : result
def Query(query):
    connec = mysqlconnect()
    result = Sql_Query(connec, query)
    db_close_connecction(connec)
    return result

# formatage: Function that formats the SQL query into a list
# Input : Data
# Output : Data
def formatage(Data):
    temp = []
    for i in range(0, len(Data)):
        temp.append(Data[i][0])
    Data = temp
    return Data

# button_connection : 
# Input : NO
# Output : NO
def button_connection():
    print("You are connected !")
    # Aller chercher dans la BDD les données - TO DO
    # Trouver l'utilisateur en question - TO DO
    # Importer les données en créant un User - TO DO

# button_create_new_account : 
# Input : NO
# Output : NO
def button_create_new_account():
    print("You want to create a new account !")
    # Go on the page where we create a new user - TO DO 
    
def Show_Account(Frame):
    Frame.destroy()
    from Compte import Create_Frame_Compte
    Create_Frame_Compte()

def verif_input_connec(mail, password, frame):
    error=0
    indication=""
    if mail=="":
        error+=1
        indication="Adress"
    elif password=="":
        error+=1
        indication="Password"
        
    if error==0:
        ID_Connection = Query("SELECT ID_User FROM User WHERE mail='"+ str(mail) +"' AND password='"+ str(password) +"';")
        ID_Connection = formatage(ID_Connection)
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
                                    command=button_create_new_account, 
                                    width=200, height=50, 
                                    font=("Arial", 20, "underline"), 
                                    fg_color="transparent", text_color="#FF764A", hover_color="#transparent",
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

    Frame.mainloop()