# http://www.packtpub.com/article/python-ldap-applications-ldap-opearations
 
# install python-ldap for windows to get this going!
 
import ldap
 
host = 'ldap://brett.com:389'
dn = 'bdemetris@brett.com'
pw = 'password'
base_dn = 'cn=users,dc=brett,dc=com'
filter = '(objectclass=person)'
# Show only activated users
# filter = '(&(memberOf=cn=workers,cn=users,dc=example,dc=com)(!(userAccountControl=66050)))'
attrs = ['givenName', 'sn', 'mail']
con = ldap.initialize(host)
 
# Bind to the server
con.simple_bind_s(dn, pw)
 
res = con.search_s(base_dn, ldap.SCOPE_SUBTREE, filter, attrs)
 
# Close the connection
con.unbind()
 
# Print the returned dictionary
print res[0]
 
for i in res:
    try:
        print i[1]['givenName'], i[1]['sn'], i[1]['mail'], "Password", i[1]['mail'],
    except Exception as ex:
        print "User is missing %s" % (ex)

# Write results into mySQL

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO user_model(FirstName, \
         LastName, UserName) \
         VALUES ('%s', '%s', '%s', '%d', '%s')" % \
         ('givenName', 'sn', 'mail')
         
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
