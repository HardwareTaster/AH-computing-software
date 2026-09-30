import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='components')

c = con.cursor()

c.execute("""SELECT * FROM components""")

for row in c:
  print('componetName', row[0])
  print('price', row[1])
  print('No.4+StarReviews', row[2])
  print('website', row[3])
c.close()