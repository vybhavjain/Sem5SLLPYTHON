
i = 0 
i = int(raw_input("Enter the value to be cubed"))

# version1
def expocube(i) : 
	return pow(i,3)

print("cubed value is ", expocube(i)) 

# version2
result = lambda i : pow(i,2)
print("Squared value using pow is ",result(i))


# version3

result = lambda i : i**2 
print("Squared value using ** is  ",result(i))


atomiclength = {1:12 , 2 : 4 , 3 : 32 , 4 :23 }

sortedlist = []

sortedlist = sorted(atomiclength.items(), key = lambda x : x[1] , reverse = True )
print sortedlist
print (len(atomiclength)) 



