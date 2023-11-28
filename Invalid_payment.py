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

def Reset_Loading():
    FileLoad = open("Loading.txt", "w")
    FileLoad.write("0")
    FileLoad.close()

#TODO --------------------------- GUI

def Recup_User():
    FileUser = open("Connect_User.txt", "r")
    var = FileUser.readline().strip()
    FileUser.close()
    return var

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

def Delete_User():
    FileUser = open("Connect_User.txt", "w")
    FileUser.close()
    
def show_Payment(Frame_Accueil, ID):
    from payment import Create_Payment_Frame
    from User_class import Card
    print("  /!\____________ DELETE CARD")
    User_Card = Card(ID, "0", "000", "01", "", "2100", "None")
    query_Delete = User_Card.Delete_Info()
    update(query_Delete)
    Frame_Accueil.destroy()
    Create_Payment_Frame()

def Create_Invalid_Payment_Frame():
    
    ID_User = Recup_User()

    Frame = CTk()
    Frame.title("Validation")
    Frame.geometry("1920x1080")

    set_appearance_mode('light')

    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=1)

    PlaneImageInvalid= "Payment Invalid Background.png"
    BackG_Image = Image.open(PlaneImageInvalid)
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
                    border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: show_Payment(Frame, ID_User))
    Btn_Home.grid(row=0, column=2, sticky='se', padx=10, pady=10)
    
    def on_closing():
        Delete_User()
        Reset_Loading()
        print("Fermeture de la page.")
        Frame.destroy()
    
    Frame.protocol("WM_DELETE_WINDOW", on_closing)

    Frame.mainloop()