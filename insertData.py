import pyodbc

try:
    con_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./RHBSME.accdb;'
    connect = pyodbc.connect(con_string)
    cursor = connect.cursor()

    cursor.execute('INSERT INTO Application(bus_id, app_id, app_status, app_date, app_approval_date)VALUES (?,?,?,?,?)')
    connect.commit()

except pyodbc.Error as e:
    print("Error in Insertion:", e)

# .executemany() if more than one row
# 'INSERT INTO Business(bus_id, bus_industry, bus_annual_revenue, bus_incorperation_date, bus_credit_score)VALUES (?,?,?,?,?)'
# 'INSERT INTO Account(acc_id,acc_email, acc_username, acc_password, acc_phone_no, bus_id)VALUES (?,?,?,?,?,?)'