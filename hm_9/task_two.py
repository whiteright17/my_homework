import csv
names_csv = 'names.csv'
new_names_csv = 'new_names.csv'
with open(names_csv, 'r') as names_csv:
    csv_reader = csv.DictReader(names_csv)
    with open(new_names_csv, 'w', newline='') as new_names:
        field_names = ['email']
        csv_writer = csv.DictWriter(new_names, fieldnames=field_names)
        csv_writer.writeheader()
        for line in csv_reader:
            new_line = {'email': line['email']}
            csv_writer.writerow(new_line)
print('Copy')
