list = [1,24,12,423,5,234,523,5,325,]
length = len(list)

multiple_lists = [[] for i in range(len(list))]

x = 0
for i in range(len(list)):
    part = min(list)
    multiple_lists[x].append(part)
    list.remove(part)
    x = x + 1

print(multiple_lists)