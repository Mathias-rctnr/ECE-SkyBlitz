from customtkinter import *
import tkinter as tk
from tkinter import messagebox, Radiobutton
from PIL import Image, ImageTk
import pymysql
from Invalid_payment import Create_Invalid_Payment_Frame
from Valid_payment import Create_Valid_Payment_Frame
from User_class import User, Card
from Flight_class import FLight
import Database as Db

# Recup_info_flight : takes the informations of a flight from a text file
# Input : No
# Output : Info
def Recup_info_flight():
    
    #0=Departure___1=Arrival___2=Hour___3=Day___4=Month_5=Year
    
    Info = []
    txtFile = open("Actual_Flight.txt", "r")
    for i in range(0, 6):
        print(i)
        Info.append(txtFile.readline().strip())
    txtFile.close()
    
    return Info

#TODO --------------------------- GUI

# show_Invalid : shows the invalid payment frame
# Input : Frame
# Output : No
def show_Invalid(Frame):
    Frame.destroy()
    Create_Invalid_Payment_Frame()

# show_Valid : shows the valid payment frame
# Input : Frame
# Output : No    
def show_Valid(Frame):
    Frame.destroy()
    Create_Valid_Payment_Frame()

# Create_Payment_Frame : creates and handles the frame for the payment
# Input : No
# Output : No     
def Create_Payment_Frame():
    
    ID_User = Db.Recup_User()
    
    Flight_Info = Recup_info_flight()
    ID_Flight = Db.Query("SELECT ID_flight from Flight Where departureAirport = '"+ Flight_Info[0] +"' AND arrivalAirport = '"+ Flight_Info[1] +"' AND departureDate_Hour = '"+ Flight_Info[2] +"' AND departureDate_Day = '"+ Flight_Info[3] +"' AND departureDate_Month = '"+  Flight_Info[4] +"' AND departureDate_Year = '"+ Flight_Info[5] +"';")
    ID_Flight = Db.formatage(ID_Flight)
    print("____________________________ID Flight = " + str(ID_Flight))
    print("____________________________Flight = " + str(Flight_Info))

    Flight_Recup = FLight(str(ID_Flight[0]), Flight_Info[0], Flight_Info[1], Flight_Info[5], Flight_Info[4], Flight_Info[3], Flight_Info[2], 0, 0, 0, 0, 0, 0, "")
    Flight_Recup.display()
    
    # verif_Payment : checks if the payment is valid or not
    # Input : name, number, month, year, cvc, frame, TypeSeat
    # Output : No 
    def verif_Payment(name, number, month, year, cvc, frame, TypeSeat):
        error = 0
        if (not name.replace(" ", "").isalpha() or not len(name)>=3):
            error+=1
        elif (not number.isdigit() or len(number)!=16):
            error+=1
        elif (month=="Month"):
            error+=1
        elif (year=="Year"):
            error+=1
        elif (not cvc.isdigit() or (len(cvc)!=3 and len(cvc)!=4)):
            error+=1
        elif (TypeSeat=="Class"):
            error+=1
        if error==0:
            Actual_User = User(ID_User, "", "", "", "", "2000", "01", "01", "", "", "", 0, "", "", 0, "")
            Card_User = Card(ID_User, number, cvc ,month, name, year, "10000")      #! /!\ BANK BALANCE HERE /!\
            if TypeSeat=="Economy":
                Flight_Price = Db.Query("SELECT economyPrice from Flight Where ID_flight = '" + str(ID_Flight[0]) + "'")
                Flight_Price = Db.formatage(Flight_Price)
            elif TypeSeat=="Business":
                Flight_Price = Db.Query("SELECT businessPrice from Flight Where ID_flight = '" + str(ID_Flight[0]) + "'")
                Flight_Price = Db.formatage(Flight_Price)
            print("Price = " + str(Flight_Price))
            #ADD_BDD(name, number, month, year, cvc, "10000")
            query_Card_Insert = Card_User.insert_in_BDD()
            Db.update(query_Card_Insert)
            Card_User.display()
            sold = Db.Query("SELECT bank_balance from CreditCard Where ID_UserCard = '" + ID_User + "'")
            sold = Db.formatage(sold)
            print("Sold: " + str(sold))
            if(sold[0]>=Flight_Price[0]):
                rest = sold[0] - Flight_Price[0]
                Card_User.bank_Balance=rest
                Passengers = Db.Query("SELECT ID_User from Flight Where departureAirport = '"+ Flight_Info[0] +"' AND arrivalAirport = '"+ Flight_Info[1] +"' AND departureDate_Hour = '"+ Flight_Info[2] +"' AND departureDate_Day = '"+ Flight_Info[3] +"' AND departureDate_Month = '"+  Flight_Info[4] +"' AND departureDate_Year = '"+ Flight_Info[5] +"';")
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
                Flight_Recup.ID_Passengers = FinalList
                query_update_Card = Card_User.update_Bank_Balance()
                Db.update(query_update_Card)
                #update("UPDATE CreditCard SET bank_balance ='"+ str(rest) +"' WHERE ID_UserCard = '"+ str(ID_User) +"';")
                
                Flight_Recup.display()
                query_update_Flight = Flight_Recup.update_Flight_Payment()
                Db.update(query_update_Flight)
                #update("UPDATE Flight SET ID_User = '" + FinalList + "' WHERE departureAirport = '" + Flight_Info[0] + "' AND arrivalAirport = '" + Flight_Info[1] + "' AND departureDate_Hour = '" + Flight_Info[2] + "' AND departureDate_Day = '" + Flight_Info[3] + "' AND departureDate_Month = '" + Flight_Info[4] + "' AND departureDate_Year = '" + Flight_Info[5] + "';")
                
                tempFuturFlight = Db.Query("Select futur_flight from user where ID_User = '"+ str(ID_User) +"';")
                tempFuturFlight = Db.formatage(tempFuturFlight)
                Actual_User.futur_Flight = tempFuturFlight[0]
                
                if len(tempFuturFlight)>0:
                    Separate_List_User = tempFuturFlight[0].split('-')
                    Flight_Recup.display()
                    Separate_List_User.append(Flight_Recup.ID_Flight)
                    print("SeparateUser: "+ str(Separate_List_User))
                else:
                    Separate_List_User=[Flight_Recup.ID_Flight]
                    
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
            messagebox.showinfo("error", "Your inputs are not correct.")

    Frame = CTk()
    Frame.title("Payment")
    Frame.geometry("1920x1080")

    set_appearance_mode('light')

    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=2)
    Frame.columnconfigure(1, weight=1)


    PlaneImage = "Payment_BG.png"
    BackG_Image = Image.open(PlaneImage)
    resized_image = BackG_Image.resize((1800, 1080), Image.ANTIALIAS)
    backG_Image_Convert = ImageTk.PhotoImage(resized_image)

    BackGround = tk.Label(Frame, image=backG_Image_Convert, width=1920, height=1080)
    BackGround.grid(row=0, column=0, columnspan=2, sticky="nsew")

    Div_Wrapper = CTkFrame(master=Frame)
    Div_Wrapper.grid(row=0, column=1, sticky='nsew')

    Div_Wrapper.rowconfigure(0, weight=1)
    Div_Wrapper.rowconfigure(1, weight=6)
    Div_Wrapper.rowconfigure(2, weight=3)
    Div_Wrapper.columnconfigure(0, weight=1)
    Div_Wrapper.columnconfigure(1, weight=6)
    Div_Wrapper.columnconfigure(2, weight=1)
    

    Price = CTkTextbox(master=Div_Wrapper, font=("Arial", 40, "bold"),  fg_color="transparent", height=10)
    FlightPriceEco = Db.Query("SELECT economyPrice from Flight Where ID_flight = '" + str(ID_Flight[0]) + "'")
    FlightPriceEco = Db.formatage(FlightPriceEco)
    FlightPriceBus = Db.Query("SELECT businessPrice from Flight Where ID_flight = '" + str(ID_Flight[0]) + "'")
    FlightPriceBus = Db.formatage(FlightPriceBus)
    Price.insert("2.0", "Eco: " + str(FlightPriceEco[0]) + "£ or Business: " + str(FlightPriceBus[0])+ "£")
    Price.configure(state="disabled")
    Price.grid(row=0, column=0, sticky='nsew', columnspan=3, padx=(50, 0), pady=(20, 0))

    Div_payment = CTkFrame(master=Div_Wrapper, fg_color="#CBCBCB", corner_radius=35, border_width=5, bg_color="transparent")
    Div_payment.grid_propagate(False)
    Div_payment.grid(row=1, column=1, sticky='nsew')

    Div_payment.rowconfigure(0, weight=1)
    Div_payment.rowconfigure(1, weight=1)
    Div_payment.rowconfigure(2, weight=1)
    Div_payment.rowconfigure(3, weight=1)
    Div_payment.rowconfigure(4, weight=1)
    Div_payment.columnconfigure(0, weight=1)
    Div_payment.columnconfigure(1, weight=1)
    Div_payment.grid_propagate(False)

    Name_Input = CTkEntry(master=Div_payment, fg_color="#DBDBDB", font=("Arial", 25, "bold"), text_color="#000000", width=380, height=80, corner_radius=40, border_width=5, border_color="#FF764A", placeholder_text="Name of the owner")
    Name_Input.grid_propagate(False)
    Name_Input.grid(row=0, column=0, sticky='n', pady=(30 ,0), columnspan=3)

    Number_Input = CTkEntry(master=Div_payment, fg_color="#DBDBDB", font=("Arial", 25, "bold"), text_color="#000000", width=380, height=80, corner_radius=40, border_width=5, border_color="#FF764A", placeholder_text="Number on the card")
    Number_Input.grid_propagate(False)
    Number_Input.grid(row=1, column=0, sticky='n', pady=(30 ,0), columnspan=3)

    Year = ["2024", "2025", "2026", "2027"]
    Month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    Month_Exp_Input = CTkOptionMenu(master=Div_payment,height=50, width=200, fg_color="#DBDBDB", dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Month, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13", anchor=CENTER)
    Month_Exp_Input.grid_propagate(False)
    Month_Exp_Input.set("Month")
    Month_Exp_Input.grid(row=2, column=0, sticky='n', pady=(30 ,0))

    Year_Exp_Input = CTkOptionMenu(master=Div_payment,height=50, width=200, fg_color="#DBDBDB", dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=Year, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13", anchor=CENTER)
    Year_Exp_Input.grid_propagate(False)
    Year_Exp_Input.set("Year")
    Year_Exp_Input.grid(row=2, column=1, sticky='n', pady=(30 ,0))

    CVC_Input = CTkEntry(master=Div_payment, fg_color="#DBDBDB", font=("Arial", 25, "bold"), text_color="#000000", width=170, height=80, corner_radius=40, border_width=5, border_color="#FF764A", placeholder_text="CVC")
    CVC_Input.grid_propagate(False)
    CVC_Input.grid(row=3, column=0, sticky='n', pady=(10 ,20), columnspan=2)
    
    ClassSeat = ["Economy", "Business"]
    
    TypeOfSeat = CTkOptionMenu(master=Div_payment,height=50, width=200, fg_color="#DBDBDB", dropdown_fg_color="#FFFFFF", font=("Arial", 25, "bold"), values=ClassSeat, text_color="#000000", button_color="#FF764A", button_hover_color="#FF4C13", anchor=CENTER)
    TypeOfSeat.grid_propagate(False)
    TypeOfSeat.set("Class")
    TypeOfSeat.grid(row=4, column=0, sticky='n', columnspan=2, pady=(0, 15))

    Btn_Validation = CTkButton(master=Div_Wrapper, text="Validate", corner_radius=50, fg_color="#FF4C13", hover_color="#FF764A",
                            width=200, height=75, border_width=6, border_color="#FF764A", font=("Arial", 30, "bold"), text_color="#FFFFFF", 
                            command=lambda: verif_Payment(Name_Input.get(), Number_Input.get(), Month_Exp_Input.get(), Year_Exp_Input.get(), CVC_Input.get(), Frame, TypeOfSeat.get()))
    Btn_Validation.grid(row=2, column=0, columnspan=3)

    # on_closing : closes the actual frame
    # Input : No
    # Output : No 
    def on_closing():
        Db.Delete_User()
        Db.Reset_Loading()
        print("Fermeture de la page.")
        Frame.destroy()
    
    Frame.protocol("WM_DELETE_WINDOW", on_closing)

    Frame.mainloop()