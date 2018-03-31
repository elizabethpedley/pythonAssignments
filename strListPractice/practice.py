words = "It's thanksgiving day. It's my birthday,too!"
x = [2,54,-2,7,12,98]
newList = []
x2 = [19,2,54,-2,7,12,98,32,10,-3,6]
newX = []
# find the position of the first 'day'
print(words.find('day'))
# replace 'day' with 'month'
print(words.replace('day', 'month'))
# the min value of x
print(min(x))
# the max value of x
print max(x)
# find the first and last value and add them to a new list
newList.append(x[0])
newList.append(x[len(x)-1])
print newList
#sort the x2
x2.sort()
print(x2)
# create a new list with the first half of x2 being at index 0
newX.append(x2[:5])

for x in x2[5:]:
    newX.append(x)

print newX



