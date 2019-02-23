#create csv file by this programs

import csv 

with open("example1.csv",'w')as obj:
    field = ["name","salary"]
    writer = csv.DictWriter(obj, fieldnames=field)

    writer.writeheader()
    writer.writerow({'name':'bob','salary':10000})
    writer.writerow({'name':'sem','salary':40000})
    writer.writerow({'name':'kamlesh','salary':30000})
    writer.writerow({'name':'vishal','salary':50000})