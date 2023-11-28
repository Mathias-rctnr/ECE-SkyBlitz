from customtkinter import *
import pymysql
from User_class import User
import datetime
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

def Reset_Loading():
    FileLoad = open("Loading.txt", "w")
    FileLoad.write("0")
    FileLoad.close()

def Verif_Input_Account(title, Firstname, Lastname, year, month, day, nationality, adress, city, postCode, country, phone, mail, password):
    error=0
    indication=""
    if title=="Title":
        error+=1
        indication="Title"
    elif Firstname=="":
        error+=1
        indication="FirstName"
    elif Lastname=="":
        error+=1
        indication="Last Name"
    elif year=="Year":
        error+=1
        indication="FirstName"
    elif month=="Month":
        error+=1
        indication="Month"
    elif day=="Day":
        error+=1
        indication="Day"
    elif adress=="":
        error+=1
        indication="Adress"
    elif city=="":
        error+=1
        indication="City"
    elif postCode=="" or not postCode.isdigit():
        error+=1
        indication="Post Code"
    elif country=="":
        error+=1
        indication="Country"
    elif phone=="" or not phone.isdigit():
        error+=1
        indication="Phone"
    elif mail=="":
        error+=1
        indication="Mail"
    elif password=="":
        error+=1
        indication="Password"
    
    if error==0:
        print("ADD in BDD")
        ID_New = Query("SELECT MAX(ID_User) FROM User;")
        ID_New = formatage(ID_New)
        ID_New = int(ID_New[0]) + 1
        print(ID_New)
        New_User = User(ID_New, title, Firstname, Lastname, mail, year, month, day, nationality, password, adress, postCode, city, country, phone, "0")
        Add_Query = New_User.save_in_database()
        update(Add_Query)
    else:
        messagebox.showinfo("error", "ERROR INPUTS: "+ str(indication))

Principal_frame = CTk()
Principal_frame.title("Skyblitz")
Principal_frame.geometry("1920x1080")

# Scrollbar frame
Frame = CTkFrame(master=Principal_frame, width=1500, height=950, corner_radius=30)
Frame.pack(pady=(100, 0))
set_appearance_mode('light')

Frame.grid_columnconfigure(0, weight=1)
Frame.grid_columnconfigure(1, weight=1)
Frame.grid_columnconfigure(2, weight=1)

Frame.grid_rowconfigure(0, weight=1)
Frame.grid_rowconfigure(1, weight=1)
Frame.grid_rowconfigure(2, weight=1)
Frame.grid_rowconfigure(3, weight=1)
Frame.grid_rowconfigure(4, weight=1)
Frame.grid_rowconfigure(5, weight=1)
Frame.grid_rowconfigure(6, weight=1)

# Orange foncé : #FF4C13
# Orange clair : #FF764A
# Gris foncé :  #DBDBDB
# Gris clair : #CBCBCB

#___________________________ TITLE

Title = CTkTextbox(master=Frame, font=("Arial", 50, "bold"), fg_color="transparent", text_color="#282828", width=400, height=80)
Title.insert("2.0", "NEW ACCOUNT")
Title.configure(state="disabled")
Title.grid(row=0, column=1)

#--------------------------- Gender Mr/Mrs
menu_title = CTkOptionMenu(master=Frame, 
                           values=["Mrs.", "M."], 
                           width=200, height=50,
                           font=("Arial", 22, "bold"), 
                           fg_color="#DBDBDB", 
                           dropdown_fg_color="#FFFFFF", 
                           text_color="#000000", 
                           button_color="#FF764A", 
                           button_hover_color="#FF4C13",
                           anchor=CENTER
                           )
menu_title.set("Title")
menu_title.grid(row=1, column=0, pady=30)

#--------------------------- First Name

firstName_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="First Name"
    )
firstName_entry.grid(row=1, column=1, padx=20, pady=30)

#--------------------------- Last Name

lastName_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="Last Name"
    )
lastName_entry.grid(row=1, column=2, padx=20, pady=30)

#--------------------------- Date of birth

Year = [str(year) for year in range(1900, 2005)]
Input_Year = CTkOptionMenu(master=Frame, values=Year, width=200, height= 50,
                            fg_color="#DBDBDB", dropdown_fg_color="#FFFFFF", text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                            font=("Arial", 22, "bold"), anchor=CENTER)
Input_Year.set("Year")
Input_Year.grid(row=2, column=0, padx=40, pady=30)

Day = [str(day) for day in range(1, 31)]
Input_Day = CTkOptionMenu(master=Frame, values=Day, width=200, height= 50,
                            fg_color="#DBDBDB", dropdown_fg_color="#FFFFFF", text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                            font=("Arial", 22, "bold"), anchor=CENTER)
Input_Day.set("Day")
Input_Day.grid(row=2, column=1, padx=20, pady=30)

Month = [str(month) for month in range(1, 12)]
Input_Month = CTkOptionMenu(master=Frame, values=Month, width=200, height= 50,
                            fg_color="#DBDBDB", dropdown_fg_color="#FFFFFF", text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                            font=("Arial", 22, "bold"), anchor=CENTER)
Input_Month.set("Month")
Input_Month.grid(row=2, column=2, padx=40, pady=30)


#--------------------------- Nationality

Nationality = ["French", "British", "German", "Italian", "American", "Canadian", "- Another -"]
nationality_input = CTkOptionMenu(master=Frame, values=Nationality, width=200, height= 50,
                            fg_color="#DBDBDB", dropdown_fg_color="#FFFFFF", text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                            font=("Arial", 22, "bold"), anchor=CENTER)
nationality_input.grid(row=3, column=0, padx=40, pady=30)

#--------------------------- Adress

adress_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="Adress"
    )
adress_entry.grid(row=3, column=1, padx=40, pady=30)

#--------------------------- City

city_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="City"
    )
city_entry.grid(row=3, column=2, padx=40, pady=30)

#--------------------------- Postcode

postcode_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="Post Code"
    )
postcode_entry.grid(row=4, column=0, padx=40, pady=30)

#--------------------------- Country

country_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="Country"
    )
country_entry.grid(row=4, column=1, padx=40, pady=30)

#--------------------------- Phone number

phone_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="Phone"
    )
phone_entry.grid(row=4, column=2, padx=40, pady=30)

#--------------------------- Email

email_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="E-Mail"
    )
email_entry.grid(row=5, column=0, pady=30)

#--------------------------- Password

password_entry = CTkEntry(
    master=Frame, 
    fg_color="#DBDBDB",
    text_color="#000000",
    font=("Arial", 22, "bold"),
    width=200, 
    height=50,
    placeholder_text="Password"
    )
password_entry.configure(show='*')
password_entry.grid(row=5, column=2, pady=30)


#--------------------------- Buttons
button_createAccount = CTkButton(Frame, 
                                text="Create",
                                width=200, height=50, 
                                font=("Arial", 20, "bold"), 
                                fg_color="#FF764A", text_color="#000000", hover_color="#FF4C13",
                                corner_radius=50, command=lambda: Verif_Input_Account(menu_title.get(), firstName_entry.get(), lastName_entry.get(), Input_Year.get(), Input_Month.get(), Input_Day.get(), nationality_input.get(), adress_entry.get(), city_entry.get(), postcode_entry.get(), country_entry.get(), phone_entry.get(), email_entry.get(), password_entry.get()))
button_createAccount.grid(row=5, column=1, padx=40, pady=30)


button_Account_existing = CTkButton(Frame, 
                                text="I already have an account", 
                                width=200, height=50, 
                                font=("Arial", 20, "underline"), 
                                fg_color="transparent", text_color="#FF764A",
                                corner_radius=50)
button_Account_existing.grid(row=6, column=1, padx=40)


Principal_frame.mainloop()


# To do :
# - Ajouter un scroll option date 
# - Enregistrer info dans database --> help
# - Comment changer de page avec les boutons (si fonction main -> comment avoir acces aux infos car je ne peux pas passer les infos en paramètres avec une commande de bouton)

# - Changer l'attribut dateNaissance par age dans User
# - Ajouter un ID dans la classe User

""" TO DO
Page d'accueil
    message d'erreur specifique à l'erreur
    erreur date du passée
"""