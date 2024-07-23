s = set()
#A set is gonna be used when all elements are unique
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)

s.remove(2) #Remove the number 2
print(s) #Only shows number 3 one time because in a set same values dont repeat

print(f"The set has {len(s)} elements.") #Getting the length of set