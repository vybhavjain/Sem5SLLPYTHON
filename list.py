a=[]#1
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)
#2
def countX(a, x): 
    count = 0
    for ele in a: 
        if (ele == x): 
            count = count + 1
    return count 
  
x = 8
print(countX(a, x)) 

#3
def Max(a):
    if len(a) <= 1:
            return a[0]
    else:
            m = Max(a[1:])
            return m if m > a[0] else a[0]


print("the largest number is: ", Max(a))

