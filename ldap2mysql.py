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
      f_name = str(result[1]['givenName'])
      f_name = f_name.replace("[","")
      f_name = f_name.replace("'","")
      f_name = f_name.replace("]","")
      print f_name
   except:
      pass
   #set sn to l_name
   try:
      l_name = str(result[1]['sn'])
      l_name = l_name.replace("[","")
      l_name = l_name.replace("'","")
      l_name = l_name.replace("]","")
      print l_name
   except:
      pass
   #set mail to mail
   try:
      mail = str(result[1]['mail'])
      mail = mail.replace("[","")
      mail = mail.replace("'","")
      mail = mail.replace("]","")
      print mail
      #execute the sql command for each. can this be outside of this particular try?
      cursor.execute("INSERT INTO user_model(FirstName, LastName, UserName) VALUES(%s,%s,%s)", [f_name, l_name, mail])
   except:
      pass



#write the variables to mySQL
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
