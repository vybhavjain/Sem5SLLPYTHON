l=["1 hello","2 there", "3 my","4 name ","5 is ","6 vybhav"]
for i in range(len(l)):
	if i%2==0:
		print(l[i])
    
for i in range(len(l)):
	if (i+1)%3==0:
		print(l[i].upper())

def reverse(string):
    string = "".join(reversed(string))
    return string

l2=[reverse(i) for i in l]
print(l2)

l4=[]
for i in range(len(l)):
    hi = l[i].split(" ")
    for x in hi:
        if x.isdigit():
            l4.append(x)
print(l4)
