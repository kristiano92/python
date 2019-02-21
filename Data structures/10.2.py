name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = list()
di = dict()
for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    time = line[5].split(':')
    h = time[0]
    hours.append(h)
#print(hours)

for h in hours:
    di[h] = di.get(h,0)+1
#print(di)
tmp = list()
for k,v in di.items():

    tmp.append((k,v))


tmp = sorted(tmp)

for k, v in tmp:
    print(k,v)
