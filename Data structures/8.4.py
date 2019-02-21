fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    word = line.split()
    for i in word:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
