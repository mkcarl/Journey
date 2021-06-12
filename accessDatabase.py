from logging import disable
import pyodbc
import matplotlib.pyplot as plt

try:
    con_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./RHBSME.accdb;'
    connect = pyodbc.connect(con_string)
    cursor = connect.cursor()
    cursor.execute('SELECT loan_amount, loan_duration, loan_amount_paid, loan_amount*((100+loan_interest_rate)/100) AS compounded_loan_amount FROM Loan WHERE bus_id = \'bus00001\'')

    rows = cursor.fetchall()[0]
    

    def graph_pie(total, paid, title):
        outstanding = float(total) - float(paid)
        labels = ['Paid', 'Outstanding']
        size= [paid, outstanding]
        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(size, explode = explode, labels = labels, shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title(title)
        plt.savefig(f"123.png")


    graph_pie(rows[3], rows[2], "Loan status of Carl Yan")
    


except pyodbc.Error as e:
    print("Error in Connection:", e)

# 'SELECT loan_amount, loan_duration, loan_amount_paid, loan_amount*((100+loan_interest_rate)/100) FROM Loan'
# 'SELECT * FROM Application'
# 'SELECT * FROM Business'

