import pyodbc

try:
    con_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./RHBSME.accdb;'
    connect = pyodbc.connect(con_string)
    print("Connected TO Database")

except pyodbc.Error as e:
    print("Error in Connection:", e)