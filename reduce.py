# from functools import reduce
wordlen = [2,3,4,2]
sum = reduce(lambda x,y : x+y ,wordlen )
print(sum)	
print(sum/len(wordlen))
