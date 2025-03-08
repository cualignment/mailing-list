import csv

# Function to process CSV and format it like formatted_mailinglist.txt
def process_csv_to_txt(csv_file_path, txt_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        with open(txt_file_path, mode='w') as txt_file:
            for row in csv_reader:
                for i in range(0, len(row), 2):
                    if row[i] and row[i+1]:
                        txt_file.write(f"{row[i+1]} {row[i]}\n")

# Example usage
process_csv_to_txt('listserv/Listserv Processing Mailing List - Sheet1.csv', 'listserv/formatted_mailinglist.txt')
