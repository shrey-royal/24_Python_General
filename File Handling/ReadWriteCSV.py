"""
CSV: Comma-Seperated Values

line 1
line 2
.
.
.
line n

record 1
record 2
.
.
.
record n

"""

import csv

# f = open('csv_file')
# csv_reader = csv.reader(f)

# for line in csv_reader:
#     print(line)
# ------------------------------------------------------------------

# with open('country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for line in csv_reader:
#         print(line)
# ------------------------------------------------------------------


# with open('country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for line_no, line in enumerate(csv_reader, 1):
#         if line_no == 1:
#             print('Header:')
#             print(line)
#             print('Data:')
#         else:
#             print(line)
# ------------------------------------------------------------------

# with open('country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
    
#     next(csv_reader)

#     for line in csv_reader:
#         print(line)
# ------------------------------------------------------------------

# total_area = 0
# with open('country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
    
#     next(csv_reader)

#     for line in csv_reader:
#         total_area += float(line[1])

# print(total_area)

'''
csv.reader() function has 2 main limitations.

1) the way of accessing the columns is not so obvious.
2) when the order of columns are changed then we also have to make changes into our python to get the right data.


hence, we use DictReader class
'''
# ------------------------------------------------------------------

# DictReader class

# with open('country.csv', 'r') as f:
#     csv_reader = csv.DictReader(f)

#     next(csv_reader)

#     for line in csv_reader:
#         print(f"The area of {line['name']} is {line['area']} km2")
# ------------------------------------------------------------------

# col_names = ['country_name', 'area', 'code2', 'code3']

# with open('country.csv', 'r') as f:
#     csv_reader = csv.DictReader(f, col_names)

#     next(csv_reader)

#     for line in csv_reader:
#         print(f"The area of {line['country_name']} is {line['area']} km2")
# ------------------------------------------------------------------

# header = ['name', 'area', 'country_code2', 'country_code3']
# data = [
#     ['Albania', 28748, 'AL', 'ALB'],
#     ['Algeria', 2381741, 'DZ', 'DZA'],
#     ['American Samoa', 199, 'AS', 'ASM'],
#     ['Andorra', 468, 'AD', 'AND'],
#     ['Angola', 1246700, 'AO', 'AGO']
# ]

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     writer.writerow(header)
#     writer.writerows(data)
# ------------------------------------------------------------------

# Renaming/Deleting a file

import os

# os.rename(src, dst): syntax
print("Before")
try:
    os.rename("countries.csv", "NoFile.csv")
    # os.remove("NoFile.csv")
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)

print("After")
