#CSVファイルの書き込み

import csv

csv_file = open('./python.csv', 'w', newline='')
writer = csv.writer(csv_file)

row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()
