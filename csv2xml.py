#      My Learning Plan Integration        #
# ---------------------------------------- #
# Define Username and Password Information #
# Define Testmode as True or False         #
# ---------------------------------------- #
mlp_id = '17204'
mlp_pw = 'xml40271api'
testmode = True

# Libraries used by MLP Script
import csv
import requests
import xml.dom

# target file.  destination file will be created
csvFile = 'C:\work\work.csv'
xmlFile = 'C:\work\myData.xml'

# open and read both files
csvData = csv.reader(open(csvFile, 'rU'))
xmlData = open(xmlFile, 'w')

# write root tag
xmlData.write('<root>' + "\n")

# write line 2 - customer id and password
if testmode == True:
    xmlData.write("<customer id='%s' password='%s' testmode='1'>" % (mlp_id,mlp_pw) + "\n")
else:
    xmlData.write("<customer id='%s' password='%s'>" % (mlp_id,mlp_pw) + "\n")

# parse csv and create the body - actions to take = _Add, _Update
rowNum = 0
refNum = 25986
for row in csvData:
    if rowNum == 0:
        tags = row
        # put tagline cleanup code here
    else:
        refNum += 1
        action = 'User_Add'
        xmlData.write("<action type='%s' ref='%s'>" % (action,str(refNum))+ "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</action>' + "\n")

    rowNum +=1

xmlData.write('</customer>' + "\n")
xmlData.write('</root>' + "\n")

# closing xml file object
xmlData.close()

# MLP Server POST Request

headers = {'Content-Type': 'text/html'}
url = 'https://www.mylearningplan.com/xml/dataexchange.asp'
xml = open(xmlFile).read()

postResponse = requests.post(url, data=xml, headers=headers, auth=(mlp_id, mlp_pw))

#Convert Unicode to String
stringResponse = str(postResponse.text)

#Split the string into a list.  Assign ref and code to variables, and clean them up 
refID = stringResponse.split()[3].replace("'","").strip('ref=')
refCode = stringResponse.split()[4].replace("'","").strip('code=').strip('>Testmode')

print refID, refCode


#write response blob to xml file and iterate
#xmlResponse = 'C:\work\Response.xml'
#xmlPush = open(xmlResponse, 'w')
#xmlPush.write(postResponse.text)
#xmlPush.close()


