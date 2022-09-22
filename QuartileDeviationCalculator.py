#CURRENTLY ONLY WORKS IF THERE ARE NO REPEATING VALUES
list = [1,24,12,423,5,234,523,325, 2, 4123, 26]
length = len(list)

multiple_lists = [[] for i in range(len(list))]

x = 0
for i in range(len(list)):
    part = min(list)
    multiple_lists[x].append(part)
    list.remove(part)
    x = x + 1


x = len(multiple_lists)

#Data is sorted into quartiles
q1 = multiple_lists[0: int((1/2*x))]

q3 = multiple_lists[int((1/2*x)): x]



q3_calculate = []
q1_calculate = []
x = 0

#Loops through quartile  and adds each data point into new list
for  i in range(len(q3)):
    part = q3[x]
    part = part[0]
    q3_calculate.append(part)
    x = x + 1

x = 0
for i in range(len(q1)):
    part = q1[x]
    part = part[0]
    q1_calculate.append(part)
    x = x + 1

# Finds the Q1 and Q2 values

half1 = int(len(q1_calculate) / 2)
q1_value = q1_calculate[half1]

half3 = int(len(q3_calculate) / 2)
q3_value = q3_calculate[half3]



# Uses quartile deviation formula to find quartile deviation
print( "Interquartile Range: "   + str(q3_value - q1_value))
print(("Quartile Deviation: " + str((q3_value - q1_value) / 2)))