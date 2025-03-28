from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
from payment import Create_Payment_Frame, show_Invalid, show_Valid
from Flight_class import FLight
from User_class import User, Card
import Database as Db

#TODO --------------------------- GUI

# Show_Account: destroys the actual frame and shows the payment
# Input : Frame
# Output : No
def show_Payment(Frame):
    Frame.destroy()
    Create_Payment_Frame()

# Show_Account: destroys the actual frame and shows the frame of the next flights
# Input : Frame
# Output : No  
def Create_Frame_Next_flights(Airport_Dep, Airport_Arriv, Year, Month, Day):
    
    ID_User = Db.Recup_User()
    
    requeteDeparture = Airport_Dep

    Frame_Accueil = CTk()
    Frame_Accueil.title("Next Flights")
    Frame_Accueil.geometry("1920x1080")

    Frame_Accueil.rowconfigure(0, weight=1)
    Frame_Accueil.rowconfigure(1, weight=9)
    Frame_Accueil.columnconfigure(0, weight=1)

    Frame_Accueil.grid_propagate(False)
    
    # Show_Account: destroys the actual frame and shows the frame of the connection
    # Input : Frame
    # Output : No  
    def show_Connection(Frame):
                Frame.destroy()
                from Connexion import Create_Connection_Frame
                Create_Connection_Frame()
    
    # Show_Account: destroys the actual frame and shows the frame of the Menu
    # Input : Frame
    # Output : No 
    def show_Menu(Frame_Accueil):
        from Accueil import Create_Frame_Menu
        Frame_Accueil.destroy()
        Create_Frame_Menu()

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
                    font=("Arial", 30, "bold"), text_color="#000000", command=lambda: show_Menu(Frame_Accueil))
    Btn_Home.grid(row=0, column=0, padx=(0, 120))

    Div_Titre = CTkLabel(master=Header, fg_color="transparent", text="", width=Frame_Accueil.winfo_screenwidth(), corner_radius=20)
    Div_Titre.grid(row=0, column = 1, sticky='nsew', pady=20)

    Title_SkyBlitz = CTkTextbox(master=Div_Titre, width=50, font=("Arial", 70, "bold"), height=40, fg_color="transparent")
    Title_SkyBlitz.insert("2.0", "NEXT FLIGHTS")
    Title_SkyBlitz.configure(state="disabled")
    Title_SkyBlitz.grid(row=0, column=0, sticky='nsew')
    Title_SkyBlitz.grid_propagate(False)


    #? AFFICHAGE VOLS
    # Show_Account: Display the "No Result" Frame
    # Input : No
    # Output : No 
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

    # Show_Account: Create a little frame for a flight
    # Input : row, deparutre Airport, Arrival Airport, Departure Hour, Departure Day, Departure Month, Departure Year, Arrival Hour
    # Output : No 
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
        DepartAirp = Db.Query("SELECT departureAirport FROM Flight")
        DepartureHour = Db.Query("SELECT departureDate_Hour FROM Flight")
        ArrivalHour = Db.Query("SELECT arrivalDate_Hour FROM Flight")
        NbFlight = Db.Query("SELECT COUNT(DISTINCT ID_flight) FROM Flight")
    else:
        DepartAirp = Db.Query("SELECT departureAirport FROM Flight WHERE departureAirport='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
        DepartureHour = Db.Query("SELECT departureDate_Hour FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
        ArrivalHour = Db.Query("SELECT arrivalDate_Hour FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
        NbFlight = Db.Query("SELECT COUNT(DISTINCT ID_flight) FROM Flight WHERE departureAirport='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartAirp = Db.formatage(DepartAirp)
    DepartureHour = Db.formatage(DepartureHour)
    ArrivalHour = Db.formatage(ArrivalHour)
    print(ArrivalHour)
    print(DepartAirp)
    print(DepartureHour)

    if Airport_Arriv=="":
        ArrivAirp = Db.Query("SELECT arrivalAirport FROM Flight")
    else:
        ArrivAirp = Db.Query("SELECT arrivalAirport FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    ArrivAirp = Db.formatage(ArrivAirp)
    print(ArrivAirp)
    
    if Day=="":
        DepartureDay = Db.Query("SELECT departureDate_Day FROM Flight")
    else:
        DepartureDay = Db.Query("SELECT departureDate_Day FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartureDay = Db.formatage(DepartureDay)
    print(DepartureDay)

    if Month=="":
        DepartureMonth = Db.Query("SELECT departureDate_Month FROM Flight")
    else:
        DepartureMonth = Db.Query("SELECT departureDate_Month FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartureMonth = Db.formatage(DepartureMonth)
    print(DepartureMonth)

    if Year=="":
        DepartureYear = Db.Query("SELECT departureDate_Year FROM Flight")
    else:
        DepartureYear = Db.Query("SELECT departureDate_Year FROM Flight WHERE departureAirport ='" + requeteDeparture + "' AND arrivalAirport = '" + Airport_Arriv + "' AND departureDate_Year = '" + str(Year) + "' AND departureDate_Day = '" + str(Day) + "' AND departureDate_Month = '" + str(Month) + "'")
    DepartureYear = Db.formatage(DepartureYear)
    print(DepartureYear)
    
    # Show_Account: Do every action for booking a flight. Create a payment frame
    # Input : index, frame
    # Output : No 
    def Booking(index, frame):
        
        if ID_User!="":
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
            
            Exist = Db.Query("SELECT COUNT(*) FROM CreditCard WHERE ID_UserCard = '"+ str(ID_User) +"';")
            Exist = Db.formatage(Exist)
            
            Already_Book =  Db.Query("SELECT ID_User from Flight Where departureAirport = '"+ str(DepartAirp[index-2]) +"' AND arrivalAirport = '"+ str(ArrivAirp[index-2]) +"' AND departureDate_Hour = '"+ str(DepartureHour[index-2]) +"' AND departureDate_Day = '"+ str(DepartureDay[index-2]) +"' AND departureDate_Month = '"+  str(DepartureMonth[index-2]) +"' AND departureDate_Year = '"+ str(DepartureYear[index-2]) +"';")
            print(Already_Book)
            if Already_Book[0][0] is not None:
                print("DAns ALREADY_BOOK IF 1")
                Already_Book = Db.formatage(Already_Book)
            else:
                print("DAns ALREADY_BOOK ELSE 1")
                Already_Book=[""]
                
            print(Already_Book)
            
            ListPassengers = Db.recup_Passenger(Already_Book)
            
            if ID_User not in ListPassengers:
                
                print("******************************* Exist User : " + str(Exist))
                print("ID_User : " + str(ID_User))
                
                if(Exist[0]==0):
                    show_Payment(frame)
                else:
                    ID_Flight = Db.Query("SELECT ID_flight from Flight Where departureAirport = '"+ str(DepartAirp[index-2]) +"' AND arrivalAirport = '"+ str(ArrivAirp[index-2]) +"' AND departureDate_Hour = '"+ str(DepartureHour[index-2]) +"' AND departureDate_Day = '"+ str(DepartureDay[index-2]) +"' AND departureDate_Month = '"+  str(DepartureMonth[index-2]) +"' AND departureDate_Year = '"+ str(DepartureYear[index-2]) +"';")
                    ID_Flight = Db.formatage(ID_Flight)
                    Flight_Price = Db.Query("SELECT economyPrice from Flight Where ID_flight = '" + str(ID_Flight[0]) + "'")
                    Flight_Price = Db.formatage(Flight_Price)
                    Flight_Select = FLight(str(ID_Flight[0]), str(DepartAirp[index-2]), str(ArrivAirp[index-2]), str(DepartureYear[index-2]), str(DepartureMonth[index-2]), str(DepartureDay[index-2]), str(DepartureHour[index-2]), "2000", "10", 0, 0, 0, 0, "")
                    Actual_User = User(ID_User, "", "", "", "", "2000", "01", "01", "", "", "", 0, "", "", 0, "")
                    Card_User = Card(ID_User, "0", "0" , "01", "name", "2000", "")
                    print("Price = " + str(Flight_Price))
                    sold = Db.Query("SELECT bank_balance from CreditCard Where ID_UserCard = '" + ID_User + "'")
                    sold = Db.formatage(sold)
                    print("Sold: " + str(sold))
                    if(sold[0]>=Flight_Price[0]):
                        rest = sold[0] - Flight_Price[0]
                        Card_User.bank_Balance=rest
                        Passengers = Db.Query("SELECT ID_User from Flight Where departureAirport = '"+ str(DepartAirp[index-2]) +"' AND arrivalAirport = '"+ str(ArrivAirp[index-2]) +"' AND departureDate_Hour = '"+ str(DepartureHour[index-2]) +"' AND departureDate_Day = '"+ str(DepartureDay[index-2]) +"' AND departureDate_Month = '"+  str(DepartureMonth[index-2]) +"' AND departureDate_Year = '"+ str(DepartureYear[index-2]) +"';")
                        Passengers = Db.formatage(Passengers)
                        print(Passengers)
                        if len(Passengers)>0:
                            ListPassengers = Db.recup_Passenger(Passengers)
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
                        Db.update(query_update_Card)
                        #update("UPDATE CreditCard SET bank_balance ='"+ str(rest) +"' WHERE ID_UserCard = '"+ str(ID_User) +"';")
                        
                        Flight_Select.display()
                        query_update_Flight = Flight_Select.update_Flight_Payment()
                        Db.update(query_update_Flight)
                        #update("UPDATE Flight SET ID_User = '" + FinalList + "' WHERE departureAirport = '" + Flight_Info[0] + "' AND arrivalAirport = '" + Flight_Info[1] + "' AND departureDate_Hour = '" + Flight_Info[2] + "' AND departureDate_Day = '" + Flight_Info[3] + "' AND departureDate_Month = '" + Flight_Info[4] + "' AND departureDate_Year = '" + Flight_Info[5] + "';")
                        
                        tempFuturFlight = Db.Query("Select futur_flight from user where ID_User = '"+ str(ID_User) +"';")
                        tempFuturFlight = Db.formatage(tempFuturFlight)
                        Actual_User.futur_Flight = tempFuturFlight[0]
                        
                        if len(tempFuturFlight)>0:
                            Separate_List_User = tempFuturFlight[0].split('-')
                            Flight_Select.display()
                            Separate_List_User.append(Flight_Select.ID_Flight)
                            print("SeparateUser: "+ str(Separate_List_User))
                        else:
                            Separate_List_User=[str(Flight_Select.ID_Flight)]
                            
                        if Separate_List_User and Separate_List_User[0] == '':
                            del Separate_List_User[0]
                            
                        FinalListUser = "-".join(Separate_List_User)
                        print(FinalListUser)
                        
                        Actual_User.futur_Flight = str(FinalListUser)
                        query_User_Flights = Actual_User.update_Futur_Flight()
                        Db.update(query_User_Flights)
                        
                        Actual_User.display()
                        
                        print("bank Acount after :" + str(rest))
                        show_Valid(frame)
                    else:
                        Card_User.display()
                        query_Delete = Card_User.Delete_Info()
                        Db.update(query_Delete)
                        #update("DELETE FROM CreditCard WHERE ID_UserCard = '"+ str(ID_User) +"';")
                        show_Invalid(frame)
            else:
                messagebox.showinfo("error", "You have already book this fly.")
        else:
            show_Connection(Frame_Accueil)


    NbFlight = Db.formatage(NbFlight)
    NbFlight = NbFlight[0]
    NbFlight = int(NbFlight)
    print(NbFlight)

    for i in range(1, NbFlight+1):
        Creation_Div_Vol(i+1, DepartAirp[i-1], ArrivAirp[i-1], DepartureHour[i-1], DepartureDay[i-1], DepartureMonth[i-1], DepartureYear[i-1], ArrivalHour[i-1])
        
    if NbFlight==0:
        No_Result()
        
    def on_closing():
        Db.Delete_User()
        Db.Reset_Loading()
        print("Fermeture de la page.")
        Frame_Accueil.destroy()
    
    Frame_Accueil.protocol("WM_DELETE_WINDOW", on_closing)

    Frame_Accueil.mainloop()