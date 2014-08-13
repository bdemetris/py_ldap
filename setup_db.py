#!/usr/bin/python
# test_db_con.py - setup for ldap_py application
#this is a test script that returns the database version on a successful connection

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","brett","password","mlpdata" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data


# Drop table if it already exist using execute() method.
# ------ > Use this for a reset (development) < -------
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE user_model (
         FirstName  CHAR(20) NOT NULL,
         LastName  CHAR(20),
         UserName CHAR(30),
         EmployeeID INT(10),
         Password CHAR(10) )"""

cursor.execute(sql)

# disconnect from server
db.close()