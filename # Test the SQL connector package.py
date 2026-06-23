# mySQL Connector SloCo INSERT Program
# Ian Simpson, October 2019

import mysql.connector
    
con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sloco')
c = con.cursor()

sqlstatement = "INSERT INTO `client` (`Client_ID`, `Name`, `Address`, `PhoneNo`, `FaxNo`) VALUES ('3', 'Dottore Ettore Ferrari', 'Via San Siro 18', '0223789543', '0278397895');"
c.execute(sqlstatement)
sqlstatement = "INSERT INTO `client` (`Client_ID`, `Name`, `Address`, `PhoneNo`, `FaxNo`) VALUES ('5', 'Anthony Gaudi', 'Via Carlo Botta 9', '33 7293748', '33 4327984');"
c.execute(sqlstatement)
sqlstatement = "INSERT INTO `client` (`Client_ID`, `Name`, `Address`, `PhoneNo`, `FaxNo`) VALUES ('2', 'Pier Ciarlante', '1 Almondvale Way', '0131 244 4330', '');"
c.execute(sqlstatement)
sqlstatement = "INSERT INTO `client` (`Client_ID`, `Name`, `Address`, `PhoneNo`, `FaxNo`) VALUES ('7', 'Anton Artikov', '67 Big street', '999', '123456789');"
c.execute(sqlstatement)

con.commit() # note it is connection, not cursor here

print(c.rowcount,"record inserted")

c.close()