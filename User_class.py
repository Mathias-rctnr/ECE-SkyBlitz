import datetime

class User():
    # Constructor
    def __init__(self, ID, title, first_name, last_name, email, yearbirth, monthbirth, daybirth, nationality, password, adress, postcode, city, country, phone_number, List_flight):
        self.ID = ID
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.yearOfBirth = yearbirth
        self.monthOfBirth = monthbirth
        self.dayOfBirth = daybirth
        self.nationality = nationality
        self.email = email
        self.password = password
        self.adress = adress
        self.postcode = postcode
        self.city = city
        self.country = country
        self.phone_number = phone_number
        self.futur_Flight = List_flight
        
        self.age = self.calculate_age(self.yearOfBirth, self.monthOfBirth, self.dayOfBirth)

    # Getters & Setters
    
    
    # Methods
    def display(self):
        print("Title: ", self.title)
        print("ID: ", self.ID)
        print("First name: ", self.first_name)
        print("Last name: ", self.last_name)
        print("Age: ", self.age)
        print("Email: ", self.email)
        print("Nationality: ", self.nationality)
        print("Password: ", self.password)
        print("Adress: ", self.adress, " - ", self.postcode, " - ", self.city, " - ", self.country)
        print("Phone: ", self.phone_number)

    def save_in_database(self):
        insert_query = "INSERT INTO user (ID_User, Title, first_name, last_name, mail, age, Nationality, password, city, postcode, country, adress, phone, futur_flight) VALUES ('"+ str(self.ID) +"','"+ str(self.title) +"','"+ str(self.first_name) +"','"+ str(self.last_name) +"','"+ str(self.email) +"','"+ str(self.age) +"','"+ str(self.nationality) +"', '"+ str(self.password) +"', '"+ str(self.city) +"', '"+ str(self.postcode) +"', '"+ str(self.country) +"', '"+ str(self.adress) +"', '"+ str(self.phone_number) +"','"+ str(self.futur_Flight) +"')"
        
        return insert_query
    
    def connection(self):
        select = "SELECT ID_User FROM User WHERE mail='"+ str(self.email) +"' AND password='"+ str(self.password) +"';"

        return select
    
    def update_Flight(self):
        query_update="Update User set futur_flight ='"+ str(self.futur_Flight) +"' WHERE ID_User='"+ str(self.ID) +"';"
        
        return query_update
    
    def update_Futur_Flight(self):
        query_update="Update User set futur_flight ='"+ str(self.futur_Flight) +"' WHERE ID_User='"+ str(self.ID) +"';"
        
        return query_update
            
    def update_Modification(self):
        query_update = "UPDATE User SET first_name = '{}', last_name = '{}', mail = '{}', password = '{}', phone = '{}', city = '{}', postcode = '{}' WHERE ID_User = '{}';".format(str(self.first_name), str(self.last_name), str(self.email), str(self.password), str(self.phone_number), str(self.city), str(self.postcode), str(self.ID))
        
        return query_update
    
    def calculate_age(self, year, month, day):
        year = int(year)
        month = int(month)
        day = int(day)
        # Create a datetime object from the entered integers
        birth_date = datetime.datetime(year, month, day)
        # Get the current date
        current_date = datetime.datetime.now()
        # Calculate the difference between the two dates
        difference = current_date - birth_date
        # Extract the years from the difference
        age = difference.days // 365

        return age
    
class Card(User):
    def __init__(self, ID, numCard, CVC, exp_month, owner, exp_year, bank):
        super().__init__(ID, "", "", "", "", "2000", "01", "01", "", "", "", "", "", "", "", [])
        self.numero = numCard
        self.CVV = CVC
        self.expiry_Month = exp_month
        self.expiry_Year = exp_year
        self.owner = owner
        self.bank_Balance = bank
        
    
    def insert_in_BDD(self):
        query = "INSERT INTO CreditCard (ID_UserCard, numero, CVC, expiryDate_Month, owner, expiryDate_Year, bank_balance) VALUES ('"+ str(self.ID) +"', '"+ str(self.numero) +"', '"+ str(self.CVV) +"', '"+ str(self.expiry_Month) +"', '"+ str(self.owner) +"', '"+ str(self.expiry_Year) +"', '"+ str(self.bank_Balance) +"');"
        
        return query
        
    def update_Bank_Balance(self):
        query_update = "UPDATE CreditCard SET bank_balance ='"+ str(self.bank_Balance) +"' WHERE ID_UserCard = '"+ str(self.ID) +"';"
        
        return query_update
    
    def Delete_Info(self):
        query_delete = "DELETE FROM CreditCard WHERE ID_UserCard = '"+ str(self.ID) +"';"
        
        return query_delete
    