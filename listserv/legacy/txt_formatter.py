import re

# Read the unformatted mailing list
with open('/home/ryanz/coding/github/mailing-list/listserv/mailinglist_unformatted.txt', 'r') as file:
    data = file.read()

# Use regex to find all email addresses and names
pattern = re.compile(r'([\w\.-]+@[\w\.-]+)\s+([\w\s]+)')
matches = pattern.findall(data)

# Format the output
formatted_data = '\n'.join([f'{email} {name}' for email, name in matches])

# Write the formatted data to a new file
with open('formatted.txt', 'w') as file:
    file.write(formatted_data)
