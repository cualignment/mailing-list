import csv

# Function to convert CSV to TXT
def csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r') as csvfile, open(txt_file, 'w') as txtfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            for i in range(0, len(row), 3):  # Adjusted to handle the CSV structure
                if i+1 < len(row) and row[i] and row[i+1]:
                    name_parts = row[i].split()
                    if len(name_parts) == 2:
                        first_name, last_name = name_parts
                    else:
                        first_name = name_parts[0]
                        last_name = ' '.join(name_parts[1:])
                    email = row[i+1]
                    txtfile.write(f'{email} {first_name} {last_name}\n')

# Convert the provided CSV to TXT
csv_to_txt('listserv/Mailing List - Sheet1.csv', 'listserv/mailinglist.txt')
