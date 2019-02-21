# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for i in fh:
    n = i.rstrip()
    print(n.upper())
