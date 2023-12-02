import pymysql

#!------------------- DATABASE              ___________________ /!\ METTRE RESET LOADING DANS TOUT LES CLOSES /!\

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

# Recup_User : reads the name of the actual User
# Input : No
# Output : var
def Recup_User():
    FileUser = open("Connect_User.txt", "r")
    var = FileUser.readline().strip()
    print(var)
    FileUser.close()
    return var

# Analyze_Loading : simulates cookies to check if the app has already been opened
# Input : No
# Output : var
def Analyze_Loading():
    FileUser = open("Loading.txt", "r")
    var = FileUser.readline().strip()
    print("Loading: " + str(var))
    FileUser.close()
    
    if var=="0":
        FileWrite = open('Loading.txt', 'w')
        FileWrite.write("1")
        FileWrite.close()
        
    return var

# Analyze_Loading : it deletes the cookies of the loading page
# Input : No
# Output : No
def Reset_Loading():
    FileLoad = open("Loading.txt", "w")
    FileLoad.write("0")
    FileLoad.close()

# Delete_User : if the user leaves, it deletes the cookies
# Input : No
# Output : No
def Delete_User():
    FileUser = open("Connect_User.txt", "w")
    FileUser.close()
    
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
        
def recup_Passenger(list):
    print("DANS LISTE RECUP PASSENGERS")
    output_list = list[0].split('-')
    return output_list