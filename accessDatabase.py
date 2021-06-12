# import pyodbc

# try:
#     con_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./RHBSME.accdb;'
#     connect = pyodbc.connect(con_string)
#     cursor = connect.cursor()
#     cursor.execute('SELECT loan_amount, loan_duration, loan_amount_paid, loan_amount*((100+loan_interest_rate)/100) AS compounded_loan_amount FROM Loan')

#     for row in cursor.fetchall():
#         print(row)

# except pyodbc.Error as e:
#     print("Error in Connection:", e)

# 'SELECT loan_amount, loan_duration, loan_amount_paid, loan_amount*((100+loan_interest_rate)/100) FROM Loan'
# 'SELECT * FROM Application'
# 'SELECT * FROM Business'
if __name__ == "__main__": 
    import pyodbc
    msa = [x for x in pyodbc.drivers() if "ACCESS" in x.upper()]
    print(msa)