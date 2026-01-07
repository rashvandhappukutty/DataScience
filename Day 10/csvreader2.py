import csv
 
def get_row_from_csv(file_path, row_index):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == row_index:
                return row
    return None
file_path = 'Day 10\Student.csv'
row_index = 3 
row = get_row_from_csv(file_path, row_index)
if row:
    print(f"Row {row_index}: {row}")
else:
    print(f"Row {row_index} not found.")