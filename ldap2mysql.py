# http://www.packtpub.com/article/python-ldap-applications-ldap-opearations
 
# install python-ldap for windows to get this going!
 
import ldap
import MySQLdb

host = 'ldap://brett.com:389'
dn = 'bdemetris@brett.com'
pw = 'Password14!'
base_dn = 'cn=users,dc=brett,dc=com'
filter = '(objectclass=person)'
# Show only activated users
# filter = '(&(memberOf=cn=workers,cn=users,dc=example,dc=com)(!(userAccountControl=66050)))'
attrs = ['givenName', 'sn', 'mail']
con = ldap.initialize(host)
 
# Bind to the AD server
con.simple_bind_s(dn, pw)

# Open MySQL database connection
db = MySQLdb.connect("localhost","brett","password","mlpdata" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create Res(ults) object 
results = con.search_s(base_dn, ldap.SCOPE_SUBTREE, filter, attrs)

# Print the returned list of tuples
# ------------> welcome to the jungle!!!
# working on this: result contains 2 objects (0 and 1), we only care about the 1st
for result in results:
#   print 'debug: result'
#   print result
   #set giveName to f_name
   try:
      f_name = result[1]['givenName']
      print f_name
   except:
      pass
   #set sn to l_name
   try:
      l_name = result[1]['sn']
      print l_name
   except:
      pass
   #set mail to mail
   try:
      mail = result[1]['mail']
      print mail
   except:
      pass
   
try:
   # Commit changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

# Close the connection
con.unbind()
