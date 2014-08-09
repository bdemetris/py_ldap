# thanks to the original author of this script!

import csv

# target file.  destination file will be created
csvFile = '/Users/$User/mlp_csv.csv'
xmlFile = '/Users/$User/Desktop/myData.xml'

# use both files
csvData = csv.reader(open(csvFile, 'rU'))
xmlData = open(xmlFile, 'w')

# write root tag
xmlData.write('<root>' + "\n")

# write line 2 - customer id and password
customer_id = 'monkey'
password = 'butts'
xmlData.write("<customer id='%s' password='%s'>" % (customer_id,password) + "\n")

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
xmlData.close()
