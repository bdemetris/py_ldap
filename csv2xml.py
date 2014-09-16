#      My Learning Plan Integration        #
# ---------------------------------------- #
# Define Username and Password Information #
# Define Testmode as True or False         #
# ---------------------------------------- #
mlp_id = 'username'
mlp_pw = 'password'
testmode = True

# Libraries used by MLP Script
import csv
import requests

# target file.  destination file will be created
csvFile = 'C:\work\work.csv'
xmlFile = 'C:\work\myData.xml'

# open and read both files
csvData = csv.reader(open(csvFile, 'rU'))
xmlData = open(xmlFile, 'w')

# write root tag
xmlData.write('<root>' + "\n")

# write line 2 - customer id and password - testmode?
if testmode == True:
    xmlData.write("<customer id='%s' password='%s' testmode='1'>" % (mlp_id,mlp_pw) + "\n")
else:
    xmlData.write("<customer id='%s' password='%s'>" % (mlp_id,mlp_pw) + "\n")

# parse csv and create the body - actions to take = _Add, _Update
rowNum = 0
refNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        refNum += 1
        action = 'User_Add'
        xmlData.write("<action type='%s' ref=%r>" % (action,str(refNum))+ "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</action>' + "\n")

    rowNum +=1

xmlData.write('</customer>' + "\n")
xmlData.write('</root>' + "\n")


# MLP Server POST Request

headers = {'Content-Type': 'text/html'}
url = 'https://www.mylearningplan.com/xml/dataexchange.asp'

postRequest = requests.post(url, data=xml, headers=headers, auth=(mlp_id, mlp_pw))


# debugging
print postRequest.text

# closing xml file object
xmlData.close()

