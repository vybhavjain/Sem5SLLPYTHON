newlist = []

def remove_duplicates(numbers):
 for number in numbers:
 	if number not in newlist:
		newlist.append(number)
 return newlist

remove_duplicates([1,2,3,4,5,6,7,6,3,2])
print newlist
