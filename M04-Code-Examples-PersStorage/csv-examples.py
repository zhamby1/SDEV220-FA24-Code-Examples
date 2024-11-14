import csv
import pandas

villians = [
  ['Doctor', 'No'],
  ['Rosa', 'Klebb'],
  ['Lex', 'Luther']
]

with open('villians.csv', "wt") as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villians)

data = pandas.read_csv('villians.csv')
print(data)
