fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From:'): continue
    line = line.split()
    mail = line[1]
    print(mail)
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
