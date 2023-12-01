from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import random
from Flight_class import FLight
from User_class import User
from payment import Create_Payment_Frame, show_Invalid, show_Valid
import matplotlib.pyplot as plt
import Database as Db

#TODO --------------------------- GUI

def show_Menu(Frame_Accueil):
        from Accueil import Create_Frame_Menu
        Frame_Accueil.destroy()
        Create_Frame_Menu()

def Convert_Month(mois):
        mois = mois.lower()
        mois_liste = ["jan", 'feb', 'mars', 'april', 'mai', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']

        if mois in mois_liste:
            return mois_liste.index(mois) + 1
        else:
            return None


def Create_Frame_Compte():
    
    def Recup_User():
        FileUser = open("Connect_User.txt", "r")
        var = FileUser.readline().strip()
        FileUser.close()
        return var

    def Delete_User():
        FileUser = open("Connect_User.txt", "w")
        FileUser.close()
        
    def Graph(ID):
        Graph_User = User(ID, "NULL", "NULL", "NULL", "NULL", "2000", "01", "01", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", 0, "NULL")
        ListOfFlights = Db.Query("Select futur_flight from user where ID_User = '"+ str(Graph_User.ID) +"';")
        ListOfFlights = Db.formatage(ListOfFlights)
        print("List of flights: " + str(ListOfFlights))
        if len(ListOfFlights)==0:   #Si la requete échoue, évite de faire une erreur
            ListOfFlights=["0"]
        Separate_Flight_User = ListOfFlights[0].split('-')
        del Separate_Flight_User[0]
        
        Int_Separate_Flight_User = [int(Separate_Flight_User) for Separate_Flight_User in Separate_Flight_User]
        print("Separate List: " + str(Int_Separate_Flight_User))
        
        Price_List_Flight = []
        abcisse = []
        for i in range(0, len(Int_Separate_Flight_User)):
            print(Int_Separate_Flight_User[i])
            abcisse.append(int(i+1))
            Price = Db.Query("Select economyPrice from Flight where ID_flight = '"+ str(Int_Separate_Flight_User[i]) +"';")
            Price = Db.formatage(Price)
            print(Price)
            Price_List_Flight.append(int(Price[0]))
        print(Price_List_Flight)
        print(abcisse)
        
        plt.figure(figsize=(10, 6))
        plt.bar(Int_Separate_Flight_User, Price_List_Flight, color='#FF764A', label='Price')

        plt.title('Graph of Prices with flights')
        plt.xlabel("ID of flights")
        plt.ylabel('Price')
        plt.legend()
        plt.show()
        
    
    def Modify():
        bg_color = Btn_Modify.cget('fg_color')
        print("Couleur de fond du bouton :", bg_color)
        
        Temp_Nom = Name.get("1.0", "end-1c")
        Temp_FamilleNom = LastName.get("1.0", "end-1c")
        Temp_Email = Mail.get("1.0", "end-1c")
        Temp_Mdp = PassWord.get("1.0", "end-1c")
        Temp_Tel = Phone.get("1.0", "end-1c")
        Temp_Ville = City.get("1.0", "end-1c")
        Temp_CodePostal = PostCode.get("1.0", "end-1c")
        Temp_Pays = Country.get("1.0", "end-1c")
        
        if bg_color=="#FF4C13":
            Btn_Modify.configure(fg_color="#FF764A")
            Btn_Modify.configure(hover_color="#FF4C13")
            
            Name.configure(state="normal")
            LastName.configure(state="normal")
            Mail.configure(state="normal")
            PassWord.configure(state="normal")
            Phone.configure(state="normal")
            City.configure(state="normal")
            PostCode.configure(state="normal")
            Country.configure(state="normal")
            
            Nom_Reduce = Temp_Nom.replace("First Name: ", "")
            FamilleNom_Reduce = Temp_FamilleNom.replace("Last Name: ", "")
            Email_Reduce = Temp_Email.replace("E-Mail: ", "")
            Mdp_Reduce = Temp_Mdp.replace("Password: ", "")
            Tel_Reduce = Temp_Tel.replace("Phone: ", "")
            Ville_Reduce = Temp_Ville.replace("City: ", "")
            CodePostal_Reduce = Temp_CodePostal.replace("Postcode: ", "")
            Pays_Reduce = Temp_Pays.replace("Country: ", "")
            
            Name.delete("0.0", "end")
            LastName.delete("0.0", "end")
            Mail.delete("0.0", "end")
            PassWord.delete("0.0", "end")
            Phone.delete("0.0", "end")
            City.delete("0.0", "end")
            PostCode.delete("0.0", "end")
            Country.delete("0.0", "end")
            
            print(Nom_Reduce)
            print(FamilleNom_Reduce)
            print(Email_Reduce)
            print(Mdp_Reduce)
            print(Tel_Reduce)
            print(Ville_Reduce)
            print(CodePostal_Reduce)
            print(Pays_Reduce)
            
            Name.insert("0.0", str(Nom_Reduce))
            LastName.insert("0.0", str(FamilleNom_Reduce))
            Mail.insert("0.0", str(Email_Reduce))
            PassWord.insert("0.0", str(Mdp_Reduce))
            Phone.insert("0.0", str(Tel_Reduce))
            City.insert("0.0", str(Ville_Reduce))
            PostCode.insert("0.0", str(CodePostal_Reduce))
            Country.insert("0.0", str(Pays_Reduce))
            
        elif bg_color=="#FF764A":
            
            Btn_Modify.configure(fg_color="#FF4C13")
            Btn_Modify.configure(hover_color="#FF764A")
            
            Nom = Name.get("1.0", "end-1c")
            FamilleNom = LastName.get("1.0", "end-1c")
            Email = Mail.get("1.0", "end-1c")
            Mdp = PassWord.get("1.0", "end-1c")
            Tel = Phone.get("1.0", "end-1c")
            Ville = City.get("1.0", "end-1c")
            CodePostal = PostCode.get("1.0", "end-1c")
            Pays = Country.get("1.0", "end-1c")
            
            MailExist = Db.Query("SELECT COUNT(*) FROM User WHERE mail = '"+ str(Email) +"' AND ID_User <> '"+ str(ID_User) +"'; ")
            MailExist = Db.formatage(MailExist)
            
            print(Nom)
            print(FamilleNom)
            print(MailExist)
            print(Mdp)
            print(Tel)
            print(Tel.isdigit())
            print(Ville)
            print(CodePostal)
            print(CodePostal.isdigit())
            print(Pays)
            
            if Nom!="" and FamilleNom!="" and MailExist[0]==0 and Mdp!="" and Tel!="" and Tel.isdigit() and Ville!="" and CodePostal!="" and CodePostal.isdigit() and Pays!="":
                Object_user = User(ID_User, "Mr.", Nom, FamilleNom, Email, "2000", "01", "01", "France", Mdp, "", CodePostal, Ville, Pays, Tel, "")
                queryUser = Object_user.update_Modification()
                Db.update(queryUser)

            else:
                messagebox.showinfo("error", "Your inputs are not correct")
                
            Name.delete("0.0", "end")
            LastName.delete("0.0", "end")
            Mail.delete("0.0", "end")
            PassWord.delete("0.0", "end")
            Phone.delete("0.0", "end")
            City.delete("0.0", "end")
            PostCode.delete("0.0", "end")
            Country.delete("0.0", "end")
            
            User_Query_Name = Db.Query("SELECT first_name FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_Name = Db.formatage(User_Query_Name)
            User_Query_LastName = Db.Query("SELECT last_name FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_LastName = Db.formatage(User_Query_LastName)
            User_Query_Mail = Db.Query("SELECT mail FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_Mail = Db.formatage(User_Query_Mail)
            User_Query_Password = Db.Query("SELECT password FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_Password = Db.formatage(User_Query_Password)
            User_Query_Phone = Db.Query("SELECT phone FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_Phone = Db.formatage(User_Query_Phone)
            User_Query_City = Db.Query("SELECT city FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_City = Db.formatage(User_Query_City)
            User_Query_PostCode = Db.Query("SELECT postcode FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_PostCode = Db.formatage(User_Query_PostCode)
            User_Query_Country = Db.Query("SELECT postcode FROM User WHERE ID_User='"+ str(ID_User) +"'")
            User_Query_Country = Db.formatage(User_Query_Country)
            Name.insert("1.0", "First Name: " + str(User_Query_Name[0]))
            LastName.insert("1.0", "Last Name: " + str(User_Query_LastName[0]))
            Mail.insert("1.0", "E-Mail: " + str(User_Query_Mail[0]))
            PassWord.insert("1.0", "Password: " + str(User_Query_Password[0]))
            Phone.insert("1.0", "Phone: " + str(User_Query_Phone[0]))
            City.insert("1.0", "City: " + str(User_Query_City[0]))
            PostCode.insert("1.0", "Postcode: " + str(User_Query_PostCode[0]))
            Country.insert("1.0", "Country: " + str(User_Query_Country[0]))
                
            Name.configure(state="disabled")
            LastName.configure(state="disabled")
            Mail.configure(state="disabled")
            PassWord.configure(state="disabled")
            Phone.configure(state="disabled")
            City.configure(state="disabled")
            PostCode.configure(state="disabled")
            Country.configure(state="disabled")
            
            
    
    ID_User = Recup_User()
    
    def verifInputAdmin(choice, depart, arrival, day, month, year, hour, time, ID, EcoPrice, BusPrice, NbEco, NbBus):
        error=0
        if depart=="":
            error+=1
            print("1")
        elif arrival=="":
            error+=1
            print("2")
        elif day=="Day":
            error+=1
            print("3")
        elif month=="Month":
            error+=1
            print("4")
        elif year=="Year":
            error+=1
            print("5")
        elif hour=="Hour":
            error+=1
            print("5")
        elif time=="AM/PM":
            error+=1
            print("6")
        elif ID=="" and (choice==1 or choice==2):
            error+=1
            print("7")
        if choice==4:
            if EcoPrice=="Eco. Price" or not EcoPrice.isdigit():
                error+=1
                print("8")
            elif BusPrice=="Bus. Price" or not BusPrice.isdigit():
                error+=1
                print("9")
            elif NbEco=="Nb. Eco. Place" or not NbEco.isdigit():
                error+=1
                print("10")
            elif NbBus=="Nb. Bus. Place" or not NbBus.isdigit():
                error+=1
                print("11")
        print("ID: " + str(ID)) #PRINT INFORMATIONS
        print("dep: " + str(depart))
        print("arri: " + str(arrival))
        print("day: " + str(day))
        print("month: " + str(month))
        print("year: " + str(year))
        print("hour: " + str(hour))
        if error==0 and choice==1:
            if time=="PM":
                hour=int(hour)+12
            month = Convert_Month(month)
            DeleteUserFlight(ID, depart, arrival, day, month, year, hour)
        elif error==0 and choice==2:
            if time=="PM":
                hour=int(hour)+12
            month = Convert_Month(month)
            Booking_Admin(ID, depart, arrival, day, month, year, hour)
        elif error==0 and choice==3:
            if time=="PM":
                hour=int(hour)+12
            month = Convert_Month(month)
            Delete_Flight(ID, depart, arrival, day, month, year, hour)
        elif error==0 and choice==4:
            if time=="PM":
                hour=int(hour)+12
            month = Convert_Month(month)
            Add_Flight(ID, depart, arrival, day, month, year, hour, EcoPrice, BusPrice, NbEco, NbBus)
        elif error!=0:
            messagebox.showinfo("error", "Your inputs are not correct")
    
    def enlever_chiffre(string, chiffre_a_enlever):
        chiffres = string.split('-')
        chiffres_filtres = [chiffre for chiffre in chiffres if chiffre != str(chiffre_a_enlever)]
        nouvelle_chaine = '-'.join(chiffres_filtres)

        return nouvelle_chaine
    
    def DeleteUserFlight(ID, depart, arrival, day, month, year, hour):
        print("DELETE")
        ID_Search_Flight = Db.Query("SELECT ID_flight from Flight Where departureAirport = '"+ str(depart) +"' AND arrivalAirport = '"+ str(arrival) +"' AND departureDate_Hour = '"+ str(hour) +"' AND departureDate_Day = '"+ str(day) +"' AND departureDate_Month = '"+  str(month) +"' AND departureDate_Year = '"+ str(year) +"';")
        ID_Search_Flight = Db.formatage(ID_Search_Flight)
        
        Book_Flight = FLight("NULL", depart, arrival, year, month, day, hour, year, "NULL", "NULL", "NULL", "NULL", "NULL", "NULL")
        Book_User = User(ID, "NULL", "NULL", "NULL", "NULL", "2000", "01", "01", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", 0, "NULL")
        
        if len(ID_Search_Flight)==0:
            messagebox.showinfo("error", "This flight doesn't exist")
        else:
            print("ID search flight:" + str(ID_Search_Flight))
            list_Passengers_Flight = Db.Query("Select ID_User from flight Where ID_flight = '" + str(ID_Search_Flight[0]) +"';")
            list_Passengers_Flight = Db.formatage(list_Passengers_Flight)
            ListOfFlights = Db.Query("Select futur_flight from user where ID_User = '"+ str(ID) +"';")
            ListOfFlights = Db.formatage(ListOfFlights)
            print("list of passengers:" + str(list_Passengers_Flight[0]))
            
            if len(list_Passengers_Flight)>0:
                Separate_List = list_Passengers_Flight[0].split('-')
                print(Separate_List)
            
            if len(ListOfFlights)>0:
                Separate_List_User = ListOfFlights[0].split('-')
                print(Separate_List_User)

            if (str(ID) in Separate_List) and (str(ID_Search_Flight[0]) in Separate_List_User):
                NewList = enlever_chiffre(list_Passengers_Flight[0], int(ID))
                Book_Flight.ID_Passengers = NewList
                Book_Flight.ID_Flight = ID_Search_Flight[0]
                query_Flight = Book_Flight.update_Flight_Passenger()
                Db.update(query_Flight)
                
                NewListUser = enlever_chiffre(ListOfFlights[0], int(ID_Search_Flight[0]))
                Book_User.futur_Flight = NewListUser
                Book_User.ID = ID
                query_User = Book_User.update_Futur_Flight()
                Db.update(query_User)
            else:
                print("ERROR NOT IN LIST")
                print("Erreur Administrateur, ID pas dans liste futur_flight ou ID_User de flight")
                messagebox.showinfo("error", "User: " + str(ID) + " is not register for this flight")
                
    def Booking_Admin(ID, depart, arrival, day, month, year, hour):
        print("Booking Admin")
        Book_Flight = FLight("NULL", depart, arrival, year, month, day, hour, year, "NULL", "NULL", "NULL", "NULL", "NULL", "NULL")
        Book_User = User(ID, "NULL", "NULL", "NULL", "NULL", "2000", "01", "01", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", 0, "NULL")
        ID_Search_Flight = Db.Query("SELECT ID_flight from Flight Where departureAirport = '"+ str(Book_Flight.departure) +"' AND arrivalAirport = '"+ str(Book_Flight.arrival) +"' AND departureDate_Hour = '"+ str(Book_Flight.departureHour) +"' AND departureDate_Day = '"+ str(Book_Flight.departureDay) +"' AND departureDate_Month = '"+  str(Book_Flight.departureMonth) +"' AND departureDate_Year = '"+ str(Book_Flight.departureYear) +"';")
        ID_Search_Flight = Db.formatage(ID_Search_Flight)
        print(ID_Search_Flight)
        Book_Flight.ID_Flight = ID_Search_Flight[0]
        print(Book_Flight.ID_Flight)
        if len(ID_Search_Flight)==0:
            messagebox.showinfo("error", "This flight doesn't exist")
        else:
            print("ID search flight: " + str(Book_Flight.ID_Flight))
            list_Passengers_Flight = Db.Query("Select ID_User from flight Where ID_flight = '" + str(Book_Flight.ID_Flight) +"';")
            list_Passengers_Flight = Db.formatage(list_Passengers_Flight)
            Book_Flight.ID_Passengers = list_Passengers_Flight[0]
            ListOfFlights = Db.Query("Select futur_flight from user where ID_User = '"+ str(Book_User.ID) +"';")
            print(ListOfFlights)
            ListOfFlights = Db.formatage(ListOfFlights)
            
            print(list_Passengers_Flight)
            print(ListOfFlights)
            
            print("len: " + str(len(ListOfFlights)))
            
            if len(list_Passengers_Flight)==0:   #Si la requete échoue, évite de faire une erreur
                list_Passengers_Flight=["0"]
            if len(ListOfFlights)==0:
                ListOfFlights=["0"]
                
            print("list of passengers:" + str(list_Passengers_Flight))
            print("List Of Flights: " + str(ListOfFlights))
            
            Separate_List = list_Passengers_Flight[0].split('-')
            Separate_List_User = ListOfFlights[0].split('-')
            print(Separate_List)
                
            if not str(ID) in Separate_List and str(ListOfFlights[0])!="0":
                #For the table flight
                Separate_List.append(str(ID))
                print(Separate_List)
                
                if Separate_List and Separate_List[0] == '':
                    del Separate_List[0]
                
                FinalList = "-".join(Separate_List)
                print(FinalList)
                Book_Flight.ID_Flight = ID_Search_Flight[0]
                Book_Flight.ID_Passengers = FinalList
                queryFlight = Book_Flight.update_User()
                print(queryFlight)
                Db.update(queryFlight)
                
                #for the table User
                print(Separate_List_User)
                print(ID_Search_Flight)
                Separate_List_User.append(str(ID_Search_Flight[0]))
                print(Separate_List_User)
                
                if Separate_List_User and Separate_List_User[0] == '':
                    del Separate_List_User[0]
                    
                print(Separate_List_User)
                
                FinalListUser = "-".join(Separate_List_User)
                print(FinalListUser)
                Book_User.futur_Flight = FinalListUser
                Book_User.ID = ID
                queryUser = Book_User.update_Flight()
                Db.update(queryUser)
            else:
                messagebox.showinfo("error", "User: " + str(ID) + " is already register on this flight or the user doesn't exist")
                
    def Delete_Flight(ID, depart, arrival, day, month, year, hour):
        print("Delete Flight")
        ID_Search_Flight = Db.Query("SELECT ID_flight from Flight Where departureAirport = '"+ str(depart) +"' AND arrivalAirport = '"+ str(arrival) +"' AND departureDate_Hour = '"+ str(hour) +"' AND departureDate_Day = '"+ str(day) +"' AND departureDate_Month = '"+  str(month) +"' AND departureDate_Year = '"+ str(year) +"';")
        ID_Search_Flight = Db.formatage(ID_Search_Flight)
        print(ID_Search_Flight)
        
        Research_Flight = FLight(ID_Search_Flight[0], depart, arrival, year, month, day, hour, year, "NULL", "NULL", "NULL", "NULL", "NULL", "NULL")

        
        if len(ID_Search_Flight)==0:
            messagebox.showinfo("error", "This flight doesn't exist")
        else:
            query_delete = Research_Flight.delete_Flight()
            print(query_delete)
            Db.update(query_delete)
            
    def Add_Flight(ID, depart, arrival, day, month, year, hour, PriceEco, PriceBus, NbEco, NbBus):
        print("ADD FLIGHT")
        Max_ID_Flight = Db.Query("SELECT MAX(ID_flight) FROM Flight;")
        Max_ID_Flight = Db.formatage(Max_ID_Flight)
        ID_New = int(Max_ID_Flight[0])+1
        
        Verif_Exist = Db.Query("SELECT ID_flight FROM Flight Where departureAirport='"+ str(depart) +"' AND arrivalAirport='"+ str(arrival) +"' AND departureDate_Year='"+ str(year) +"' AND departureDate_Month='"+ str(month) +"' AND departureDate_Day='"+ str(day) +"' AND departureDate_Hour='"+ str(hour) +"'")
        Verif_Exist = Db.formatage(Verif_Exist)
        
        print(Verif_Exist)
        
        arrivalHour=0
        while arrivalHour<int(hour):
            arrivalHour = random.randint(1, 23) #Fake Hour for the flight
        
        if len(Verif_Exist)==0:
            New_Flight = FLight(ID_New, depart, arrival, year, month, day, hour, year, arrivalHour, PriceEco, PriceBus, NbEco, NbBus, "")
            query_Flight = New_Flight.save_in_database()
            print(query_Flight)
            Db.update(query_Flight)
        else:
            messagebox.showinfo("error", "This flight already exist")
    
    def Recup_Account():
        Info=[]
        tempName = Db.Query("SELECT first_name FROM User WHERE ID_User ="+ ID_User +";")
        tempName = Db.formatage(tempName)
        Info.append(tempName[0])
        tempLastName = Db.Query("SELECT last_name FROM User WHERE ID_User ="+ ID_User +";")
        tempLastName = Db.formatage(tempLastName)
        Info.append(tempLastName[0])
        tempmail = Db.Query("SELECT mail FROM User WHERE ID_User ="+ ID_User +";")
        tempmail = Db.formatage(tempmail)
        Info.append(tempmail[0])
        tempPassword = Db.Query("SELECT password FROM User WHERE ID_User ="+ ID_User +";")
        tempPassword = Db.formatage(tempPassword)
        Info.append(tempPassword[0])
        tempPhone = Db.Query("SELECT phone FROM User WHERE ID_User ="+ ID_User +";")
        tempPhone = Db.formatage(tempPhone)
        Info.append(tempPhone[0])
        tempCity = Db.Query("SELECT city FROM User WHERE ID_User ="+ ID_User +";")
        tempCity = Db.formatage(tempCity)
        Info.append(tempCity[0])
        tempPostCode = Db.Query("SELECT postcode FROM User WHERE ID_User ="+ ID_User +";")
        tempPostCode = Db.formatage(tempPostCode)
        Info.append(tempPostCode[0])
        tempCountry = Db.Query("SELECT country FROM User WHERE ID_User ="+ ID_User +";")
        tempCountry = Db.formatage(tempCountry)
        Info.append(tempCountry[0])
        tempAdress = Db.Query("SELECT adress FROM User WHERE ID_User ="+ ID_User +";")
        tempAdress = Db.formatage(tempAdress)
        Info.append(tempAdress[0])
        tempAge = Db.Query("SELECT age FROM User WHERE ID_User ="+ ID_User +";")
        tempAge = Db.formatage(tempAge)
        Info.append(tempAge[0])
        
        return Info
    
    def Recup_Flight(ID):
        print(ID)
        Flight=[]
        if int(ID)!=0:
            tempDepart = Db.Query("SELECT departureAirport FROM Flight WHERE ID_flight ="+ ID +";")
            tempDepart = Db.formatage(tempDepart)
            Flight.append(tempDepart[0])
            tempArrival = Db.Query("SELECT arrivalAirport FROM Flight WHERE ID_flight ="+ ID +";")
            tempArrival = Db.formatage(tempArrival)
            Flight.append(tempArrival[0])
            tempYear = Db.Query("SELECT departureDate_Year FROM Flight WHERE ID_flight ="+ ID +";")
            tempYear = Db.formatage(tempYear)
            Flight.append(tempYear[0])
            tempMonth = Db.Query("SELECT departureDate_Month FROM Flight WHERE ID_flight ="+ ID +";")
            tempMonth = Db.formatage(tempMonth)
            Flight.append(tempMonth[0])
            tempDay = Db.Query("SELECT departureDate_Day FROM Flight WHERE ID_flight ="+ ID +";")
            tempDay = Db.formatage(tempDay)
            Flight.append(tempDay[0])
            tempHour = Db.Query("SELECT departureDate_Hour FROM Flight WHERE ID_flight ="+ ID +";")
            tempHour = Db.formatage(tempHour)
            Flight.append(tempHour[0])
        
            return Flight

    Info_User = Recup_Account()

    Frame_Accueil = CTk(fg_color="#282828")
    Frame_Accueil.title("Account")
    Frame_Accueil.geometry("1920x1080")

    Frame_Accueil.rowconfigure(0, weight=1)
    Frame_Accueil.rowconfigure(1, weight=9)
    Frame_Accueil.columnconfigure(0, weight=1)

    Frame_Accueil.grid_propagate(False)

    Canvas = CTkScrollableFrame(master=Frame_Accueil, fg_color="transparent")
    Canvas.grid(row=1, column=0, sticky='nsew')
    
    Canvas.rowconfigure(0, weight=1)
    Canvas.rowconfigure(1, weight=1)
    Canvas.columnconfigure(0, weight=1)
    Canvas.columnconfigure(1, weight=6)
    Canvas.columnconfigure(2, weight=1)
    
    set_appearance_mode('light')

    Header = CTkLabel(master=Frame_Accueil, fg_color="transparent", text="", width=Frame_Accueil.winfo_screenwidth(), height=80)
    Header.grid(row=0, column = 0, sticky="nsew")

    Header.grid_propagate(False)

    Header.rowconfigure(0, weight=1)
    Header.columnconfigure(0, weight=2)
    Header.columnconfigure(1, weight=1)
    Header.columnconfigure(2, weight=2)

    Btn_Home = CTkButton(master=Header, text="HOME", corner_radius=50, fg_color="#FFFFFF", width=200, height=75, hover_color="#FF764A",
                    font=("Arial", 30, "bold"), text_color="#000000", command=lambda: show_Menu(Frame_Accueil))
    Btn_Home.grid(row=0, column=0, padx=(0, 120))

    Div_Titre = CTkLabel(master=Header, fg_color="transparent", text="", width=Frame_Accueil.winfo_screenwidth(), corner_radius=20)
    Div_Titre.grid(row=0, column = 1, sticky='nsew', pady=20)

    Title_ACCOUNT = CTkTextbox(master=Div_Titre, width=50, font=("Arial", 70, "bold"), height=40, fg_color="transparent", text_color="#FFFFFF")
    Title_ACCOUNT.insert("2.0", "ACCOUNT")
    Title_ACCOUNT.configure(state="disabled")
    Title_ACCOUNT.grid(row=0, column=0, sticky='nsew', padx=(60, 0))
    Title_ACCOUNT.grid_propagate(False)

    Div_Informations = CTkFrame(master=Canvas, fg_color="#CBCBCB", height=600)
    Div_Informations.grid(row=0, column=1, sticky="nsew")
    
    Div_Informations.rowconfigure(0, weight=1)
    Div_Informations.rowconfigure(1, weight=1)
    Div_Informations.rowconfigure(2, weight=1)
    Div_Informations.rowconfigure(3, weight=1)
    Div_Informations.rowconfigure(4, weight=1)
    Div_Informations.rowconfigure(5, weight=1)
    Div_Informations.rowconfigure(6, weight=1)
    Div_Informations.columnconfigure(0, weight=1)
    Div_Informations.columnconfigure(1, weight=1)
    Div_Informations.columnconfigure(2, weight=1)
    Div_Informations.columnconfigure(3, weight=1)
    
    Title_Info = CTkTextbox(master=Div_Informations, font=("Arial", 70, "bold"), fg_color="transparent", text_color="#282828", width=600)
    Title_Info.insert("2.0", "INFORMATIONS")
    Title_Info.configure(state="disabled")
    Title_Info.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=(400, 0), pady=(40, 0))
    
    #_____FIRST NAME
    
    Name = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    Name.insert("0.0", "First Name: "+ str(Info_User[0]))
    Name.configure(state="disabled")
    Name.grid_propagate(False)
    Name.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=(40, 0), pady=(0, 25))
    
    #_____LAST NAME
    
    LastName = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    LastName.insert("0.0", "Last Name: "+ str(Info_User[1]))
    LastName.configure(state="disabled")
    LastName.grid_propagate(False)
    LastName.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=(0, 40), pady=(0, 40))
    
    #_____EMAIL ADRESS
    
    Mail = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    Mail.insert("0.0", "E-Mail: "+ str(Info_User[2]))
    Mail.configure(state="disabled")
    Mail.grid_propagate(False)
    Mail.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=(40, 0), pady=(0, 40))
    
    #_____PASSWORD
    
    PassWord = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    PassWord.insert("0.0", "Password: "+ str(Info_User[3]))
    PassWord.configure(state="disabled")
    PassWord.grid_propagate(False)
    PassWord.grid(row=2, column=2, columnspan=2, sticky="nsew", padx=(0, 40), pady=(0, 40))
    
    #_____ADRESS
    
    Adress = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    Adress.insert("0.0", "Adress: "+ str(Info_User[8]))
    Adress.configure(state="disabled")
    Adress.grid_propagate(False)
    Adress.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=(40, 0), pady=(0, 40))
    
    #_____PHONE
    
    Phone = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    Phone.insert("0.0", "Phone: "+ str(Info_User[4]))
    Phone.configure(state="disabled")
    Phone.grid_propagate(False)
    Phone.grid(row=3, column=2, columnspan=2, sticky="nsew", padx=(0, 40), pady=(0, 40))
    
    #_____CITY
    
    City = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    City.insert("0.0", "City: "+ str(Info_User[5]))
    City.configure(state="disabled")
    City.grid_propagate(False)
    City.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=(40, 0), pady=(0, 40))
    
    #_____POSTCODE
    
    PostCode = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    PostCode.insert("0.0", "Postcode: " + str(Info_User[6]))
    PostCode.configure(state="disabled")
    PostCode.grid_propagate(False)
    PostCode.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=(0, 40), pady=(0, 40))
    
    #_____COUNTRY
    
    Country = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    Country.insert("0.0", "Country: " + str(Info_User[7]))
    Country.configure(state="disabled")
    Country.grid_propagate(False)
    Country.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=(40, 0), pady=(0, 40))
    
    #_____STATUS
    
    if Info_User[9]>=18 and Info_User[9]<65:
        status = "Adult"
    elif Info_User[9]>=65:
        status = "Senior"
    else:
        status = "NaN"
    
    Status = CTkTextbox(master=Div_Informations, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=300)
    Status.insert("0.0", "Status: " + str(status))
    Status.configure(state="disabled")
    Status.grid_propagate(False)
    Status.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=(0, 40), pady=(0, 40))
        
    #_____BUTTON
    
    Btn_Modify = CTkButton(master=Div_Informations, text="Modify", corner_radius=50, fg_color="#FF4C13", hover_color="#FF764A", width=200, height=75, border_width=6,
                    border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: Modify())
    Btn_Modify.grid(row=6, column=0, columnspan=4, padx=(0, 40), pady=30)
    
    #! DIV FLIGHTS
    
    Div_Flights = CTkFrame(master=Canvas, fg_color="#CBCBCB", height=600)
    Div_Flights.grid(row=1, column=1, sticky="nsew", pady=75)
    
    Div_Flights.rowconfigure(0, weight=1)
    Div_Flights.rowconfigure(1, weight=4)
    Div_Flights.columnconfigure(0, weight=5)
    Div_Flights.columnconfigure(1, weight=5)
    
    Title_FLIGHTS = CTkTextbox(master=Div_Flights, font=("Arial", 70, "bold"), fg_color="transparent", text_color="#282828", width=500, height=50)
    Title_FLIGHTS.insert("2.0", "FLIGHTS")
    Title_FLIGHTS.configure(state="disabled")
    Title_FLIGHTS.grid_propagate(False)
    Title_FLIGHTS.grid(row=0, column=0, sticky='nsew', padx=(520, 0), pady=(20, 30))
    
    if int(ID_User)>=0:
        Div_Print_Flights = CTkScrollableFrame(master=Div_Flights)
        Div_Print_Flights.grid(row=1, column=0, sticky="nsew")
        
        ID_Flights = Db.Query("SELECT futur_flight FROM User WHERE ID_User ="+ ID_User +";")
        ID_Flights = Db.formatage(ID_Flights)
        list_flight = Db.recup_Passenger(ID_Flights)
        print(list_flight)
        
        Flight = CTkTextbox(master=Div_Print_Flights, font=("Arial", 50, "bold"), fg_color="transparent", text_color="#282828", height=10, width=1000)
        Flight.insert("0.0", "Your flights...")
        Flight.configure(state="disabled")
        Flight.grid(row=1, column=0, sticky="nsew", pady=(0, 40), padx=(250, 0))
        
        for i in range(0, len(list_flight)-1):
            Info_Flight = Recup_Flight(list_flight[i+1])
            print(Info_Flight)
            Flight = CTkTextbox(master=Div_Print_Flights, font=("Arial", 35, "bold"), fg_color="transparent", text_color="#282828", height=10, width=1000)
            Flight.insert("0.0", str(i+1) + ": From " + str(Info_Flight[0]) + " to " + str(Info_Flight[1]) + " the " + str(Info_Flight[4]) + "/"+ str(Info_Flight[3]) + "/" + str(Info_Flight[2]) + " at " + str(Info_Flight[5]) + "H00.")
            Flight.configure(state="disabled")
            Flight.grid(row=2+i, column=0, sticky="nsew", pady=(0, 20), padx=(20, 0))
        
        Btn_Graph = CTkButton(master=Div_Flights, text="Graphics", corner_radius=50, fg_color="#FF4C13", hover_color="#FF764A", border_width=6,
                        border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: Graph(ID_User))
        Btn_Graph.grid(row=1, column=1, sticky="nsew")
    
    elif int(ID_User)<0:
        
        Year = ["2023", "2024", "2025"]
        Month = ["jan", 'feb', 'mars', 'april', 'mai', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        Day = [str(i) for i in range(1, 32)]
        Hour = [str(i) for i in range(1, 13)]
        TypeHour = ["AM", "PM"]
        
        Div_Entry_Admin = CTkFrame(master=Div_Flights)
        Div_Entry_Admin.grid(row=1, column=0, columnspan=2, sticky='nsew')
        
        for i in range(0, 9):
            Div_Entry_Admin.rowconfigure(i, weight=1)
            if i<3:
                Div_Entry_Admin.columnconfigure(i, weight=1)
        
        EntryDepart = CTkEntry(master=Div_Entry_Admin, fg_color="#CBCBCB", font=("Arial", 25, "bold"), text_color="#000000", width=280, height=60, border_color="#FF764A", border_width=5, corner_radius=30, placeholder_text="departure (AITA)")
        EntryDepart.grid(row=1, column=0, padx=10, pady=30)
        
        EntryArrival = CTkEntry(master=Div_Entry_Admin, fg_color="#CBCBCB", font=("Arial", 25, "bold"), text_color="#000000", width=280, height=60, border_color="#FF764A", border_width=5, corner_radius=30, placeholder_text="Arrival (AITA)")
        EntryArrival.grid(row=1, column=1, padx=10, pady=30)
        
        EntryID = CTkEntry(master=Div_Entry_Admin, fg_color="#CBCBCB", font=("Arial", 25, "bold"), text_color="#000000", width=200, height=60, border_color="#FF764A", border_width=5, corner_radius=30, placeholder_text="ID of User")
        EntryID.grid(row=1, column=2, padx=10, pady=30)
        
        Entry_Year = CTkOptionMenu(master=Div_Entry_Admin, fg_color="#CBCBCB", width=200, height=50,
                                dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Year, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                anchor=CENTER)
        Entry_Year.set("Year")
        Entry_Year.grid(row=2, column=0, padx=10, pady=30)

        Entry_Month = CTkOptionMenu(master=Div_Entry_Admin, fg_color="#CBCBCB", width=200, height=50,
                                    dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Month, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                    anchor=CENTER)
        Entry_Month.set("Month")
        Entry_Month.grid(row=2, column=1, padx=10, pady=30)

        Entry_Day = CTkOptionMenu(master=Div_Entry_Admin, fg_color="#CBCBCB", width=200, height=50,
                                    dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Day, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                    anchor=CENTER)
        Entry_Day.set("Day")
        Entry_Day.grid(row=2, column=2, padx=10, pady=30)
        
        Entry_Hour = CTkOptionMenu(master=Div_Entry_Admin, fg_color="#CBCBCB", width=200, height=50,
                                    dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Hour, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                    anchor=CENTER)
        Entry_Hour.set("Hour")
        Entry_Hour.grid(row=3, column=0, padx=(400, 0), pady=30)
        
        Entry_Type = CTkOptionMenu(master=Div_Entry_Admin, fg_color="#CBCBCB", width=200, height=50,
                                    dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=TypeHour, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13",
                                    anchor=CENTER)
        Entry_Type.set("AM/PM")
        Entry_Type.grid(row=3, column=2, padx=(0, 400), pady=30)
        
        EntryPriceEco = CTkEntry(master=Div_Entry_Admin, fg_color="#CBCBCB", font=("Arial", 25, "bold"), text_color="#000000", width=280, height=60, border_color="#FF764A", border_width=5, corner_radius=30, placeholder_text="Eco. Price")
        EntryPriceEco.grid(row=4, column=0, padx=10, pady=30)
        
        EntryPriceBus = CTkEntry(master=Div_Entry_Admin, fg_color="#CBCBCB", font=("Arial", 25, "bold"), text_color="#000000", width=280, height=60, border_color="#FF764A", border_width=5, corner_radius=30, placeholder_text="Bus. Price")
        EntryPriceBus.grid(row=4, column=2, padx=10, pady=30)
        
        Entry_Nb_Place_ECO = CTkEntry(master=Div_Entry_Admin, fg_color="#CBCBCB", font=("Arial", 25, "bold"), text_color="#000000", width=280, height=60, border_color="#FF764A", border_width=5, corner_radius=30, placeholder_text="Nb. Eco. Place")
        Entry_Nb_Place_ECO.grid(row=5, column=0, padx=10, pady=30)
        
        Entry_Nb_Place_BUS = CTkEntry(master=Div_Entry_Admin, fg_color="#CBCBCB", font=("Arial", 25, "bold"), text_color="#000000", width=280, height=60, border_color="#FF764A", border_width=5, corner_radius=30, placeholder_text="Nb. Bus. Place")
        Entry_Nb_Place_BUS.grid(row=5, column=2, padx=10, pady=30)
        
        Btn_Delete = CTkButton(master=Div_Entry_Admin, width=200, height=60, text="Delete User", corner_radius=40, fg_color="#FF4C13", hover_color="#FF764A", border_width=5,
                        border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: verifInputAdmin(1, EntryDepart.get(), EntryArrival.get(), Entry_Day.get(), Entry_Month.get(), Entry_Year.get(), Entry_Hour.get(), Entry_Type.get(), EntryID.get(), EntryPriceEco.get(), EntryPriceBus.get(), Entry_Nb_Place_ECO.get(), Entry_Nb_Place_BUS.get()))
        Btn_Delete.grid(row=6, column=0, pady=30)
        
        Btn_Add = CTkButton(master=Div_Entry_Admin, width=200, height=60, text="Book", corner_radius=40, fg_color="#FF4C13", hover_color="#FF764A", border_width=5,
                        border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: verifInputAdmin(2, EntryDepart.get(), EntryArrival.get(), Entry_Day.get(), Entry_Month.get(), Entry_Year.get(), Entry_Hour.get(), Entry_Type.get(), EntryID.get(), EntryPriceEco.get(), EntryPriceBus.get(), Entry_Nb_Place_ECO.get(), Entry_Nb_Place_BUS.get()))
        Btn_Add.grid(row=6, column=1, pady=30)
        
        Btn_Update = CTkButton(master=Div_Entry_Admin, width=200, height=60, text="Delete Flight", corner_radius=40, fg_color="#FF4C13", hover_color="#FF764A", border_width=5,
                        border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: verifInputAdmin(3, EntryDepart.get(), EntryArrival.get(), Entry_Day.get(), Entry_Month.get(), Entry_Year.get(), Entry_Hour.get(), Entry_Type.get(), EntryID.get(), EntryPriceEco.get(), EntryPriceBus.get(), Entry_Nb_Place_ECO.get(), Entry_Nb_Place_BUS.get()))
        Btn_Update.grid(row=6, column=2, pady=30)
        
        Btn_Add_Flight= CTkButton(master=Div_Entry_Admin, width=200, height=60, text="Add Flight", corner_radius=40, fg_color="#FF4C13", hover_color="#FF764A", border_width=5,
                        border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", command=lambda: verifInputAdmin(4, EntryDepart.get(), EntryArrival.get(), Entry_Day.get(), Entry_Month.get(), Entry_Year.get(), Entry_Hour.get(), Entry_Type.get(), EntryID.get(), EntryPriceEco.get(), EntryPriceBus.get(), Entry_Nb_Place_ECO.get(), Entry_Nb_Place_BUS.get()))
        Btn_Add_Flight.grid(row=7, column=1, pady=30)
    
    
    def on_closing():
        Delete_User()
        Db.Reset_Loading()
        print("Fermeture de la page.")
        Frame_Accueil.destroy()
    
    Frame_Accueil.protocol("WM_DELETE_WINDOW", on_closing)

    Frame_Accueil.mainloop()