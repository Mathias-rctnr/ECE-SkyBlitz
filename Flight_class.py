class FLight():
    # Constructor
    def __init__(self, ID, departure, arrival, dep_year, dep_month, dep_day, dep_hour, arrival_year, arrival_hour, eco_Price, bus_Price, seat_eco, seat_bus, ID_User):
        self.ID_Flight = ID
        self.departure = departure
        self.arrival = arrival
        self.departureYear = dep_year
        self.departureMonth = dep_month
        self.departureDay = dep_day
        self.departureHour = dep_hour
        self.arrivalYear = arrival_year
        self.arrivalHour = arrival_hour
        self.Price_Economic = eco_Price
        self.Price_Bussiness = bus_Price
        self.Seat_Economic = seat_eco
        self.Seat_Business = seat_bus
        self.ID_Passengers = ID_User    
    
    # Methods
    # display : displays the informations of a flight
    # Input : self
    # Output : No
    def display(self):
        print("ID: ", self.ID_Flight)
        print("Departure: ", self.departure)
        print("Arrival: ", self.arrival)
        print("Departure Year: ", self.departureYear)
        print("Departure Month: ", self.departureMonth)
        print("Departure Day: ", self.departureDay)
        print("Departure Hour: ", self.departureHour)
        print("Arrival Year: ", self.arrivalYear)
        print("Arrival Hour: ", self.arrivalHour)
        print("Price Economic: ", self.Price_Economic)
        print("Price Bussiness: ", self.Price_Bussiness)
        print("Seat Economic: ", self.Seat_Economic)
        print("Seat Bussiness: ", self.Seat_Business)
        print("List of passengers: ", self.ID_Passengers)

    # save_in_database : save a flight in the database
    # Input : self
    # Output : insert_query    
    def save_in_database(self):
        insert_query = requete = "INSERT INTO Flight (ID_flight, departureAirport, arrivalAirport, departureDate_Year, arrivalDate_Year, arrivalDate_Hour, economyPrice, businessPrice, availableSeatEco, availableSeatBusiness, departureDate_Month, departureDate_Day, departureDate_Hour) VALUES ('"+str(self.ID_Flight) +"', '"+ str(self.departure) +"', '"+ str(self.arrival) +"', '"+ str(self.departureYear) +"', '"+str(self.arrivalYear)+"', '"+ str(self.arrivalHour) +"', '"+ str(self.Price_Economic) +"', '"+ str(self.Price_Bussiness) +"', '"+ str(self.Seat_Economic) +"', '"+ str(self.Seat_Business)+"', '"+ str(self.departureMonth) +"', '"+ str(self.departureDay) +"', '"+ str(self.departureHour) +"');"
        
        return insert_query
    
    # delete_Flight : deletes a flight in the database
    # Input : self
    # Output : delete_query 
    def delete_Flight(self):
        delete_query = "DELETE FROM Flight WHERE ID_flight ='"+ str(self.ID_Flight) +"';"
        
        return delete_query
    
    # update_User : updates a flight in the flight table in the database
    # Input : self
    # Output : update_query
    def update_User(self):
        update_query = "Update flight set ID_User='"+ str(self.ID_Passengers) +"' WHERE ID_Flight='"+ str(self.ID_Flight) +"';"
        
        return update_query
    
    # update_Flight_Passenger : updates a flight in the user table in the database
    # Input : self
    # Output : query_update
    def update_Flight_Passenger(self):
        query_update = "Update flight set ID_User='"+ str(self.ID_Passengers) +"' WHERE ID_Flight='"+ str(self.ID_Flight) +"';"
        
        return query_update
    
    # update_Flight_Payment : updates the passenger list in the database
    # Input : self
    # Output : query_update
    def update_Flight_Payment(self):
        query_update = "UPDATE Flight SET ID_User = '" + str(self.ID_Passengers) + "' WHERE departureAirport = '" + str(self.departure) + "' AND arrivalAirport = '" + str(self.arrival) + "' AND departureDate_Hour = '" + str(self.departureHour) + "' AND departureDate_Day = '" + str(self.departureDay) + "' AND departureDate_Month = '" + str(self.departureMonth) + "' AND departureDate_Year = '" + str(self.departureYear) + "';"
        
        return query_update
