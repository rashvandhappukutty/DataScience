import csv
with open ("Day 10/Student.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Name','Age','College'])
    csvwriter.writerow(['Rashvandh',20,'KPR'])
    csvwriter.writerow(['Prathiv',23,'KPR'])
    csvwriter.writerow(['Divya',20,'KPR'])
    csvwriter.writerow(['Raagavi',20,'KPR'])