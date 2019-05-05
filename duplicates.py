import Pandas as pd
import csv
# read the file
data = pd.read_csv(
    "python_project/subscribers.csv",                # a relative path
    sep=';',                                         # values are separated by ;
    dtype={"Address": string}, {"Opt-in": string}, {"Sent Date": string},
    usecols=['Address', 'Opt-in', 'Sent Date', 'Name'],      # load only these columns
    na_values=['//', '??'])                          # ignore these characters as NA

df = pd.DataFrame(d,columns=['Address','Name'])
df

df ["is_duplicate"] = df.duplicated()
pd


# create a dictionary from the data
        (column ['address'])
         def list_duplicates(seq):
            seen = set()
            seen_add = seen.add
            # adds all elements that are duplicate to seen_twice
            seen_twice = set( x for x in seq if x in seen or seen_add(x) )
            # return the list of duplicates
            return list( seen_twice )

# Check if the entry in seen_twice meets the requirement
if
fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

# create 2 lists
# List

# maybe this way:
from datetime import date
import io

data = io.open('export_840377_1_en-4cc7d3.csv', 'r', encoding='utf8').readlines()

previous_addresses = set()

with io.open('result.csv', 'w', encoding='utf8') as output:
    output.write(data[0].strip())
    output.write(';mehet\n')

    for line in data[1:]:
        linedata = line.strip().split(';')
        if linedata[2].strip() == '' and linedata[-2] == 'True':
            if linedata[1] in previous_addresses:
                linedata[2] = '1970-01-01'
                linedata.append('nem')
                print(linedata[0])
            else:
                previous_addresses.add(linedata[1])
                linedata[2] = str(date.today())
                linedata.append('igen')
            output.write(';'.join(linedata) + '\n')
