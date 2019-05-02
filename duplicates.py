import csv
with open('./quotes.csv', 'r') as_filehandler:
    csv_file_reader = csv.DictReader(_filehandler)
    for row in csv_file_reader:
         def list_duplicates(seq):
            seen = set()
            seen_add = seen.add
        # adds all elements it doesn't know yet to seen and all other to seen_twice
            seen_twice = set( x for x in seq if x in seen or seen_add(x) )
        # turn the set into a list (as requested)
            return list( seen_twice )

a = [1,2,3,2,1,5,6,5,5,5]
list_duplicates(a) # yields [1, 2, 5]