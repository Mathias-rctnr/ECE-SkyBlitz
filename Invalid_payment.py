from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import pymysql

#!------------------- DATABASE

def mysqlconnect():
    conn = pymysql.connect(
    host='localhost',
    user='root',
    db='bdd_skyblitz',
    port=8080
)
    return conn

def Sql_Query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    output = cur.fetchall()
    return output

def db_close_connecction(conn):
    conn.close()

def Query(query):
    connec = mysqlconnect()
    result = Sql_Query(connec, query)
    db_close_connecction(connec)
    return result

#TODO --------------------------- GUI

def Recup_User():
    FileUser = open("Connect_User.txt", "r")
    var = FileUser.readline().strip()
    FileUser.close()
    return var

ID_User = Recup_User()

def Delete_User():
    FileUser = open("Connect_User.txt", "w")
    FileUser.close()

def Create_Invalid_Payment_Frame():

    Frame = CTk()
    Frame.title("Validation")
    Frame.geometry("1920x1080")

    set_appearance_mode('light')

    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=1)

    PlaneImage = "Payment Invalid Background.png"
    BackG_Image = Image.open(PlaneImage)
    resized_image = BackG_Image.resize((1700, 1080), Image.ANTIALIAS)
    backG_Image_Convert = ImageTk.PhotoImage(resized_image)

    BackGround = tk.Label(Frame, image=backG_Image_Convert, width=1920, height=1080)
    BackGround.grid(row=0, column=0, sticky="nsew")

    Div_Texte = CTkFrame(master=Frame, width=950, height=100, corner_radius=40, fg_color="#DBDBDB", border_color="#CBCBCB", border_width=5, bg_color="#EADFC1")
    Div_Texte.grid(row=0, column=0, sticky="s", pady=(0, 20))

    Div_Texte.rowconfigure(0, weight=1)
    Div_Texte.columnconfigure(0, weight=3)
    Div_Texte.columnconfigure(1, weight=3)
    Div_Texte.columnconfigure(2, weight=1)

    Div_Texte.grid_propagate(False)

    Text = CTkTextbox(master=Div_Texte, font=("Arial", 40, "bold"),  fg_color="transparent", height=50, width=800)
    Text.insert("1.0", "Your payment has been declined...")
    Text.configure(state="disabled")
    Text.grid_propagate(False)
    Text.grid(row=0, column=0, columnspan=2, sticky='se', padx=(50, 0), pady=(0, 20))

    Btn_Home = CTkButton(master=Div_Texte, text="RETRY", corner_radius=25, fg_color="#FF4C13", hover_color="#FFFFFF", width=200, height=90, border_width=6,
                    border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF")
    Btn_Home.grid(row=0, column=2, sticky='se', padx=10, pady=10)
    
    def on_closing():
        Delete_User()
        print("Fermeture de la page.")
        Frame.destroy()
    
    Frame.protocol("WM_DELETE_WINDOW", on_closing)

    Frame.mainloop()