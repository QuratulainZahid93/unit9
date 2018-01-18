filename = 'unit10_2.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))

    filename = 'unit10_2.txt'

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        # Get rid of newline, then replace Python with C.
        print(line.rstrip().replace('Python', 'C'))