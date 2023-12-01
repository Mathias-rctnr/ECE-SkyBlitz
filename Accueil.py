from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Next_Flights import Create_Frame_Next_flights
import datetime
import Database as Db

#TODO --------------------------- GUI

def Create_Frame_Menu():
    
    ID_User = Db.Recup_User()
    
    print("____________ID_______: " + str(ID_User))

    Frame = CTk()
    Frame.title("Menu")
    Frame.geometry("1920x1080")

    set_appearance_mode('light')

    Frame.rowconfigure(0, weight=1)
    Frame.rowconfigure(1, weight=17)
    Frame.rowconfigure(2, weight=5)
    Frame.columnconfigure(0, weight=1)

    def show_next_flights(Frame):
        Frame.destroy()
        Create_Frame_Next_flights("", "", "", "", "")
        
    def VerifDate():
        Today = datetime.date.today()
        Mois = Convert_Month(Input_Month.get())
        if (Today.year<int(Input_Year.get())):
            return True
        elif Today.month<Mois:
            return True
        elif Today.day<int(Input_Day.get()):
            return True
        else:
            return False
        
    def show_Connection(Frame):
        Frame.destroy()
        from Connexion import Create_Connection_Frame
        Create_Connection_Frame()
        
    def Verif_Input(Frame):
        if ((Departure_Input.get()!="Departure") and (Arrival_Input.get()!="Arrival") and (Input_Year.get()!="Year") and (Input_Month.get()!="Month") and (Input_Day.get()!="Day")) and (VerifDate()):
            show_next_flights_Research(Frame)
        elif VerifDate()==False:
            messagebox.showinfo("error", "Your date are too old")
        else:
            messagebox.showinfo("error", "Your inputs are not correct.")
            
    def VerifConnection(ID, Frame):
        if ID=="":
            print("Pas de Connexion")
            show_Connection(Frame)
        else:
            print("Connection")
            Frame.destroy()
            from Compte import Create_Frame_Compte
            Create_Frame_Compte()
    
        
    def show_next_flights_Research(Frame):
        Frame.destroy()
        Mois = Convert_Month(Input_Month.get())
        Create_Frame_Next_flights(Departure_Input.get(), Arrival_Input.get(), Input_Year.get(), Mois, Input_Day.get())

    #! --------------------- Image Background

    PlaneImage = "Fond Avion Paiement Python Project.png"
    BackG_Image = Image.open(PlaneImage)
    resized_image = BackG_Image.resize((1920, 1080), Image.ANTIALIAS)
    backG_Image_Convert = ImageTk.PhotoImage(resized_image)

    BackGround = tk.Label(Frame, image=backG_Image_Convert, width=1920, height=1080)
    BackGround.grid(row=0, column=0, rowspan=3, sticky="nsew")

    #? --------------------- HEADER


    Header = CTkLabel(master=Frame, fg_color="#F3EDE0", text="")
    Header.grid(row=0, column = 0, sticky="nsew")

    Div_btn_Header = CTkLabel(master=Header, fg_color="transparent", text="")
    Div_btn_Header.grid(row=0, column=0, sticky = "e")

    Title_SkyBlitz = CTkTextbox(master=Header, width=400, font=("Arial", 70, "bold"), height=40, fg_color="transparent")
    Title_SkyBlitz.insert("2.0", "SKYBLITZ")
    Title_SkyBlitz.configure(state="disabled")
    Title_SkyBlitz.grid(row=0, column=0, sticky='w', padx=(20, 0))


    btn_Book = CTkButton(master=Div_btn_Header, text="BOOK", corner_radius=50, fg_color="transparent", hover_color="#FF764A", width=200, height=75,
                    font=("Arial", 30, "bold"), text_color="#000000", command=lambda: show_next_flights(Frame))
    btn_Book.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)

    btn_Account = CTkButton(master=Div_btn_Header, text="ACCOUNT", corner_radius=50, fg_color="#FF4C13", hover_color="#FF764A", width=200, height=75, border_width=6,
                    border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: VerifConnection(ID_User, Frame))
    btn_Account.grid(row=0, column=1, sticky="nsew", padx=(0, 40), pady=10)


    #? --------------------- DIV BOOKING

    Departure_Data = Db.Query("SELECT DISTINCT departureAirport FROM Flight ORDER BY departureAirport;")

    Tuple_Departure = []
    for i in range(0, len(Departure_Data)):
        Tuple_Departure.append(Departure_Data[i][0])
        
    Departure_Data = Tuple_Departure


    Arrival_Data = Db.Query("select distinct arrivalAirport from Flight ORDER BY arrivalAirport;")

    Tuple_Arrival = []
    for i in range(0, len(Arrival_Data)):
        Tuple_Arrival.append(Arrival_Data[i][0])
        
    Arrival_Data = Tuple_Arrival

    Year = ["2023", "2024", "2025"]
    Month = ["jan", 'feb', 'mars', 'april', 'mai', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
    Day = [str(i) for i in range(1, 32)]
    
    def Convert_Month(mois):
        mois = mois.lower()
        mois_liste = ["jan", 'feb', 'mars', 'april', 'mai', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']

        if mois in mois_liste:
            return mois_liste.index(mois) + 1
        else:
            return None


    Div_Booking = CTkFrame(master=Frame, fg_color="#CBCBCB", width=(Frame.winfo_screenwidth()*0.75), height=250, corner_radius=35, border_width=5, bg_color="transparent")
    Div_Booking.grid(row=2, column=0)

    Div_Booking.grid_propagate(False)

    Div_Booking.rowconfigure(0, weight=3)
    Div_Booking.rowconfigure(1, weight=2)
    Div_Booking.columnconfigure(0, weight=1)
    Div_Booking.columnconfigure(1, weight=1)
    Div_Booking.columnconfigure(2, weight=3)

    Departure_Input = CTkOptionMenu(master=Div_Booking, fg_color="#DBDBDB", width=((Div_Booking.winfo_screenwidth()/4)*0.55), height=((Div_Booking.winfo_screenmmheight()/4)*0.7),
                                dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Departure_Data, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                anchor=CENTER)
    Departure_Input.set("Departure")
    Departure_Input.grid(row=0, column=0, padx=(20, 5))

    Arrival_Input = CTkOptionMenu(master=Div_Booking, fg_color="#DBDBDB", width=((Div_Booking.winfo_screenwidth()/4)*0.55), height=((Div_Booking.winfo_screenmmheight()/4)*0.7),
                                dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Arrival_Data, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                anchor=CENTER)
    Arrival_Input.set("Arrival")
    Arrival_Input.grid(row=0, column=1, padx=(5, 5))

    Div_Date_Input = CTkFrame(master=Div_Booking, fg_color="transparent", width=(Div_Booking.winfo_screenwidth()/2)*0.8, height=(Div_Booking.winfo_screenmmheight()/4)*0.7)
    Div_Date_Input.grid(row=0, column=2, padx=(5, 10))

    Div_Date_Input.pack_propagate(False)

    Input_Year = CTkOptionMenu(master=Div_Date_Input, fg_color="#DBDBDB", width=((Div_Booking.winfo_screenwidth()/6)*0.6), height=((Div_Booking.winfo_screenmmheight()/4)*0.7),
                                dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Year, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                anchor=CENTER)
    Input_Year.set("Year")
    Input_Year.pack(side = LEFT, padx=(0, 30))

    Input_Month = CTkOptionMenu(master=Div_Date_Input, fg_color="#DBDBDB", width=((Div_Booking.winfo_screenwidth()/6)*0.6), height=((Div_Booking.winfo_screenmmheight()/4)*0.7),
                                dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Month, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                anchor=CENTER)
    Input_Month.set("Month")
    Input_Month.pack(side = LEFT, padx=30)

    Input_Day = CTkOptionMenu(master=Div_Date_Input, fg_color="#DBDBDB", width=((Div_Booking.winfo_screenwidth()/6)*0.6), height=((Div_Booking.winfo_screenmmheight()/4)*0.7),
                                dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Day, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                anchor=CENTER)
    Input_Day.set("Day")
    Input_Day.pack(side = LEFT, padx=(30,0))

    Btn_Validation = CTkButton(master=Div_Booking, text="Validate", corner_radius=50, fg_color="#FF4C13", hover_color="#FF764A", width=200, height=75, border_width=6,
                    border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: Verif_Input(Frame))
    Btn_Validation.grid(row=1, column=0, columnspan=3)
    
    print(Departure_Input.get())
    
    def on_closing():
        Db.Delete_User()
        Db.Reset_Loading()
        print("Fermeture de la page.")
        Frame.destroy()
    
    Frame.protocol("WM_DELETE_WINDOW", on_closing)

    Frame.mainloop()

if Db.Analyze_Loading()=="0":
    Create_Frame_Menu()