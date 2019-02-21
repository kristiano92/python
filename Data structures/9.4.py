name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mails = list()
counts = dict()
for i in handle:
    if not i.startswith('From '):continue
    i = i.split()
    mails.append(i[1])

for mail in mails:
    counts[mail] = counts.get(mail,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
    
