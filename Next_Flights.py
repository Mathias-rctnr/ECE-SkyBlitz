from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
#from Accueil import Create_Frame_Menu
from payment import Create_Payment_Frame, update, show_Invalid, show_Valid
from Flight_class import FLight
from User_class import User, Card

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

def db_close_connection(conn):
    conn.close()

def Query(query):
    connec = mysqlconnect()
    result = Sql_Query(connec, query)
    db_close_connection(connec)
    return result

def formatage(Data):
    temp = []
    for i in range(0, len(Data)):
        temp.append(Data[i][0])
    Data = temp
    return Data

def recup_Passenger(list):
    print("DANS LISTE RECUP PASSENGERS")
    output_list = list[0].split('-')
    return output_list

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

def show_Payment(Frame):
    Frame.destroy()
    Create_Payment_Frame()

def Create_Frame_Next_flights(Airport_Dep, Airport_Arriv, Year, Month, Day):
    
    requeteDeparture = Airport_Dep

    Frame_Accueil = CTk()
    Frame_Accueil.title("Next Flights")
    Frame_Accueil.geometry("1920x1080")

    Frame_Accueil.rowconfigure(0, weight=1)
    Frame_Accueil.rowconfigure(1, weight=9)
    Frame_Accueil.columnconfigure(0, weight=1)

    Frame_Accueil.grid_propagate(False)
    
    """ def show_Menu(Frame_Accueil):
        Frame_Accueil.destroy()
        Create_Frame_Menu() """

    Canvas = CTkScrollableFrame(master=Frame_Accueil, fg_color="transparent")
    Canvas.grid(row=1, column=0, sticky='nsew')

    set_appearance_mode('light')

    Header = CTkLabel(master=Frame_Accueil, fg_color="transparent", text="", width=Frame_Accueil.winfo_screenwidth(), height=80)
    Header.grid(row=0, column = 0, sticky="nsew")

    Header.grid_propagate(False)

    Header.rowconfigure(0, weight=1)
    Header.columnconfigure(0, weight=2)
    Header.columnconfigure(1, weight=1)
    Header.columnconfigure(2, weight=2)

    Btn_Home = CTkButton(master=Header, text="HOME", corner_radius=50, fg_color="transparent", width=200, height=75, hover_color="#FF764A",
                    font=("Arial", 30, "bold"), text_color="#000000")#, command=lambda: show_Menu(Frame_Accueil))
    Btn_Home.grid(row=0, column=0, padx=(0, 120))

    Div_Titre = CTkLabel(master=Header, fg_color="transparent", text="", width=Frame_Accueil.winfo_screenwidth(), corner_radius=20)
    Div_Titre.grid(row=0, column = 1, sticky='nsew', pady=20)

    Title_SkyBlitz = CTkTextbox(master=Div_Titre, width=50, font=("Arial", 70, "bold"), height=40, fg_color="transparent")
    Title_SkyBlitz.insert("2.0", "NEXT FLIGHTS")
    Title_SkyBlitz.configure(state="disabled")
    Title_SkyBlitz.grid(row=0, column=0, sticky='nsew')
    Title_SkyBlitz.grid_propagate(False)


    #? AFFICHAGE VOLS
    
    def No_Result():
        
        Div_Result = CTkFrame(master=Canvas, fg_color="#CBCBCB", width=(Frame_Accueil.winfo_screenwidth()*0.65), height=200, corner_radius=35, border_width=5, bg_color="transparent")
        Div_Result.grid_propagate(False)
        Div_Result.grid(row=2, column=0, sticky='nsew', pady=(30, 0), padx = (270, 0))
        
        Div_Result.rowconfigure(0, weight=1)
        Div_Result.rowconfigure(1, weight=1)
        Div_Result.rowconfigure(2, weight=1)
        Div_Result.columnconfigure(0, weight=1)
        Div_Result.columnconfigure(1, weight=2)
        Div_Result.columnconfigure(2, weight=1)
        
        TitreDeparture = CTkTextbox(master=Div_Result, font=("Arial", 50, "bold"), fg_color="transparent", height=13)
        TitreDeparture.insert("1.0", "No result found.")
        TitreDeparture.configure(state="disabled")
        TitreDeparture.grid_propagate(False)
        TitreDeparture.grid(row=1, column=1, sticky='nsew')

    def Creation_Div_Vol(lig, departureAirp, arrivalAirp, Dep_hour ,Dep_day, Dep_month, Dep_year, Arriv_hour):

        Div_Result = CTkFrame(master=Canvas, fg_color="#CBCBCB", width=(Frame_Accueil.winfo_screenwidth()*0.65), height=200, corner_radius=35, border_width=5, bg_color="transparent")
        Div_Result.grid_propagate(False)
        Div_Result.grid(row=lig, column=0, sticky='nsew', pady=(30, 0), padx = (270, 0))

        Div_Result.rowconfigure(0, weight=1)
        Div_Result.rowconfigure(1, weight=2)
        Div_Result.rowconfigure(2, weight=2)
        Div_Result.rowconfigure(3, weight=2)
        Div_Result.rowconfigure(4, weight=2)
        Div_Result.rowconfigure(5, weight=2)
        Div_Result.columnconfigure(0, weight=3)
        Div_Result.columnconfigure(1, weight=3)
        Div_Result.columnconfigure(2, weight=2)

        TitreDeparture = CTkTextbox(master=Div_Result, font=("Arial", 40, "bold"), fg_color="transparent", height=13)
        TitreDeparture.insert("1.0", departureAirp)
        TitreDeparture.configure(state="disabled")
        TitreDeparture.grid_propagate(False)
        TitreDeparture.grid(row=0, column=0)

        DateDeparture = CTkTextbox(master=Div_Result, font=("Arial", 35), fg_color="transparent", height=6)
        DateDeparture.insert("1.0", str(Dep_day)+'/'+str(Dep_month)+'/'+str(Dep_year)+" - "+str(Dep_hour)+"H00")
        DateDeparture.configure(state="disabled")
        DateDeparture.grid_propagate(False)
        DateDeparture.grid(row=1, column=0, sticky='nsew', padx=(20, 0), pady=(0,10))

        TitreArrival = CTkTextbox(master=Div_Result, font=("Arial", 40, "bold"), fg_color="transparent", height=13)
        TitreArrival.insert("1.0", arrivalAirp)
        TitreArrival.configure(state="disabled")
        TitreArrival.grid_propagate(False)
        TitreArrival.grid(row=0, column=1, pady=20)

        DateArrival = CTkTextbox(master=Div_Result, font=("Arial", 35), fg_color="transparent", height=6)
        DateArrival.insert("1.0", str(Dep_day)+'/'+str(Dep_month)+'/'+str(Dep_year)+" - "+str(Arriv_hour)+"H00")
        DateArrival.configure(state="disabled")
        DateArrival.grid_propagate(False)
        DateArrival.grid(row=1, column=1, sticky='nsew', pady=(0,10))

        Btn_Book = CTkButton(master=Div_Result, text="BOOK", corner_radius=25, fg_color="#FF4C13", hover_color="#FFFFFF", width=200, height=190, border_width=6,
                        border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: Booking(lig, Frame_Accueil))
        Btn_Book.grid(row=0, column=2, rowspan=2, sticky='se', padx=10, pady=10)
        
    #* --------------- REQUETE SQL POUR AFFICHAGE
    
    if Airport_Dep=="":
        print("ENTREE")
        DepartAirp = Query("SELECT departureAirport FROM Flight")
        DepartureHour = Query("SELECT departureDate_Hour FROM Flight")
        ArrivalHour = Query("SELECT arrivalDate_Hour FROM Flight")
        NbFlight = Query("SELECT COUNT(DISTINCT ID_flight) FROM Flight")
    else:
        DepartAirp = Query("SELECT departureAirport FROM Flight WHERE departureAirport='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
        DepartureHour = Query("SELECT departureDate_Hour FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
        ArrivalHour = Query("SELECT arrivalDate_Hour FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
        NbFlight = Query("SELECT COUNT(DISTINCT ID_flight) FROM Flight WHERE departureAirport='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartAirp = formatage(DepartAirp)
    DepartureHour = formatage(DepartureHour)
    ArrivalHour = formatage(ArrivalHour)
    print(ArrivalHour)
    print(DepartAirp)
    print(DepartureHour)

    if Airport_Arriv=="":
        ArrivAirp = Query("SELECT arrivalAirport FROM Flight")
    else:
        ArrivAirp = Query("SELECT arrivalAirport FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    ArrivAirp = formatage(ArrivAirp)
    print(ArrivAirp)
    
    if Day=="":
        DepartureDay = Query("SELECT departureDate_Day FROM Flight")
    else:
        DepartureDay = Query("SELECT departureDate_Day FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartureDay = formatage(DepartureDay)
    print(DepartureDay)

    if Month=="":
        DepartureMonth = Query("SELECT departureDate_Month FROM Flight")
    else:
        DepartureMonth = Query("SELECT departureDate_Month FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartureMonth = formatage(DepartureMonth)
    print(DepartureMonth)

    if Year=="":
        DepartureYear = Query("SELECT departureDate_Year FROM Flight")
    else:
        DepartureYear = Query("SELECT departureDate_Year FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartureYear = formatage(DepartureYear)
    print(DepartureYear)
    
    def Booking(index, frame):
        
        #Delete previous text 
        fichier_Suppr = open('Actual_Flight.txt', 'w')
        fichier_Suppr.close()
        
        fichier_Flight = open('Actual_Flight.txt', 'w')
        fichier_Flight.write(str(DepartAirp[index-2]))
        fichier_Flight.write("\n")
        fichier_Flight.write(str(ArrivAirp[index-2]))
        fichier_Flight.write("\n")
        fichier_Flight.write(str(DepartureHour[index-2]))
        fichier_Flight.write("\n")
        fichier_Flight.write(str(DepartureDay[index-2]))
        fichier_Flight.write("\n")
        fichier_Flight.write(str(DepartureMonth[index-2]))
        fichier_Flight.write("\n")
        fichier_Flight.write(str(DepartureYear[index-2]))
        fichier_Flight.write("\n")
        
        fichier_Flight.close()
        
        Exist = Query("SELECT COUNT(*) FROM CreditCard WHERE ID_UserCard = '"+ ID_User +"';")
        Exist = formatage(Exist)
        
        Already_Book =  Query("SELECT ID_User from Flight Where departureAirport = '"+ str(DepartAirp[index-2]) +"' AND arrivalAirport = '"+ str(ArrivAirp[index-2]) +"' AND departureDate_Hour = '"+ str(DepartureHour[index-2]) +"' AND departureDate_Day = '"+ str(DepartureDay[index-2]) +"' AND departureDate_Month = '"+  str(DepartureMonth[index-2]) +"' AND departureDate_Year = '"+ str(DepartureYear[index-2]) +"';")
        print(Already_Book)
        if Already_Book[0][0] is not None:
            print("DAns ALREADY_BOOK IF 1")
            Already_Book = formatage(Already_Book)
        else:
            print("DAns ALREADY_BOOK ELSE 1")
            Already_Book=[""]
            
        print(Already_Book)
        
        ListPassengers = recup_Passenger(Already_Book)
        
        if ID_User not in ListPassengers:
            if(Exist[0]==0):
                show_Payment(frame)
            else:
                ID_Flight = Query("SELECT ID_flight from Flight Where departureAirport = '"+ str(DepartAirp[index-2]) +"' AND arrivalAirport = '"+ str(ArrivAirp[index-2]) +"' AND departureDate_Hour = '"+ str(DepartureHour[index-2]) +"' AND departureDate_Day = '"+ str(DepartureDay[index-2]) +"' AND departureDate_Month = '"+  str(DepartureMonth[index-2]) +"' AND departureDate_Year = '"+ str(DepartureYear[index-2]) +"';")
                ID_Flight = formatage(ID_Flight)
                Flight_Price = Query("SELECT economyPrice from Flight Where ID_flight = '" + str(ID_Flight[0]) + "'")
                Flight_Price = formatage(Flight_Price)
                Flight_Select = FLight(str(ID_Flight[0]), str(DepartAirp[index-2]), str(ArrivAirp[index-2]), str(DepartureYear[index-2]), str(DepartureMonth[index-2]), str(DepartureDay[index-2]), str(DepartureHour[index-2]), "2000", "10", 0, 0, 0, 0, "")
                Actual_User = User(ID_User, "", "", "", "", "2000", "01", "01", "", "", "", 0, "", "", 0, "")
                Card_User = Card(ID_User, "0", "0" , "01", "name", "2000", "")
                print("Price = " + str(Flight_Price))
                sold = Query("SELECT bank_balance from CreditCard Where ID_UserCard = '" + ID_User + "'")
                sold = formatage(sold)
                print("Sold: " + str(sold))
                if(sold[0]>=Flight_Price[0]):
                    rest = sold[0] - Flight_Price[0]
                    Card_User.bank_Balance=rest
                    Passengers = Query("SELECT ID_User from Flight Where departureAirport = '"+ str(DepartAirp[index-2]) +"' AND arrivalAirport = '"+ str(ArrivAirp[index-2]) +"' AND departureDate_Hour = '"+ str(DepartureHour[index-2]) +"' AND departureDate_Day = '"+ str(DepartureDay[index-2]) +"' AND departureDate_Month = '"+  str(DepartureMonth[index-2]) +"' AND departureDate_Year = '"+ str(DepartureYear[index-2]) +"';")
                    Passengers = formatage(Passengers)
                    print(Passengers)
                    if len(Passengers)>0:
                        ListPassengers = recup_Passenger(Passengers)
                        ListPassengers.append(str(ID_User))
                        print("List of passengers: "+ str(ListPassengers))
                    else:
                        ListPassengers=[str(Actual_User.ID)]
                    print(ListPassengers)
                    
                    if ListPassengers and ListPassengers[0] == '':
                        del ListPassengers[0]
                    
                    FinalList = "-".join(ListPassengers)
                    Flight_Select.ID_Passengers = FinalList
                    print(FinalList)
                    query_update_Card = Card_User.update_Bank_Balance()
                    update(query_update_Card)
                    #update("UPDATE CreditCard SET bank_balance ='"+ str(rest) +"' WHERE ID_UserCard = '"+ str(ID_User) +"';")
                    
                    Flight_Select.display()
                    query_update_Flight = Flight_Select.update_Flight_Payment()
                    update(query_update_Flight)
                    #update("UPDATE Flight SET ID_User = '" + FinalList + "' WHERE departureAirport = '" + Flight_Info[0] + "' AND arrivalAirport = '" + Flight_Info[1] + "' AND departureDate_Hour = '" + Flight_Info[2] + "' AND departureDate_Day = '" + Flight_Info[3] + "' AND departureDate_Month = '" + Flight_Info[4] + "' AND departureDate_Year = '" + Flight_Info[5] + "';")
                    
                    tempFuturFlight = Query("Select futur_flight from user where ID_User = '"+ str(ID_User) +"';")
                    tempFuturFlight = formatage(tempFuturFlight)
                    Actual_User.futur_Flight = tempFuturFlight[0]
                    
                    if len(tempFuturFlight)>0:
                        Separate_List_User = tempFuturFlight[0].split('-')
                        Flight_Select.display()
                        Separate_List_User.append(Flight_Select.ID_Flight[0])
                        print("SeparateUser: "+ str(Separate_List_User))
                    else:
                        Separate_List_User=[Flight_Select.ID_Flight]
                        
                    if Separate_List_User and Separate_List_User[0] == '':
                        del Separate_List_User[0]
                        
                    FinalListUser = "-".join(Separate_List_User)
                    print(FinalListUser)
                    
                    Actual_User.futur_Flight = str(FinalListUser)
                    query_User_Flights = Actual_User.update_Futur_Flight()
                    update(query_User_Flights)
                    
                    Actual_User.display()
                    
                    print("bank Acount after :" + str(rest))
                    show_Valid(frame)
                else:
                    Card_User.display()
                    query_Delete = Card_User.Delete_Info()
                    update(query_Delete)
                    #update("DELETE FROM CreditCard WHERE ID_UserCard = '"+ str(ID_User) +"';")
                    show_Invalid(frame)
        else:
            messagebox.showinfo("error", "You have already book this fly.")


    NbFlight = formatage(NbFlight)
    NbFlight = NbFlight[0]
    NbFlight = int(NbFlight)
    print(NbFlight)

    for i in range(1, NbFlight+1):
        Creation_Div_Vol(i+1, DepartAirp[i-1], ArrivAirp[i-1], DepartureHour[i-1], DepartureDay[i-1], DepartureMonth[i-1], DepartureYear[i-1], ArrivalHour[i-1])
        
    if NbFlight==0:
        No_Result()
        
    def on_closing():
        Delete_User()
        print("Fermeture de la page.")
        Frame_Accueil.destroy()
    
    Frame_Accueil.protocol("WM_DELETE_WINDOW", on_closing)

    Frame_Accueil.mainloop()