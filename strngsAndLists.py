words = "It's thanksgiving day. It's my birthday,too!"       
#s = "On the other hand, you have different fingers."

indexNum = words.find("day")
print indexNum 

print words.replace("thanksgiving", "easter")


x = [2,54,-2,7,12,98]
print min(x)
print max(x)

newList  = [19,2,54,-2,7,12,98,32,10,-3,6]
newList.sort()
print newList

y = ["hello",2,54,-2,7,12,98,"world"]

w = ["hello",2,54,-2,7,12,98,"world"]

#***************************************************************

changes = words.find("day")
print words.replace("day","month")

print min(x)
print max(x)

i = min(y)
j = max(y)
print "{}, {}".format(y[0],j)

w.sort()
a1 = w[:len(w) / 2]
b2 = w[len(w) / 2:]
print a1
print b2
print [a1] + b2