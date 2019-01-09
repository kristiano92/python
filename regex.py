import re
fh = open("regex_sum_150265.txt")
lst = []
score = 0
for line in fh:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    lst = lst + num
    
for i in lst:
    score = score + int(i)
print(score)
