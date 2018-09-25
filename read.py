#1a)Write a python program to read a file(txt) and count the number of times each word appears in the text file.

#1b)Search for a particular word and display the status of its existence(yes/no) and if yes, tell the number of times it appears. 

#tip: use words as key value pair in dictionary (like the , this , etc...) 

'''
count=0
file = open('vybhav.txt', 'r') 
##print file.read() 


n = int(raw_input("input the number of words you want to search for."))
list=[]

for i in range(n):
 test = raw_input('Enter the words: \n')
 list.append(test)

 
with open('vybhav.txt') as f:
    for x in range(n):
        for line in f:
	 count += line.count(list[x])
	print 'count is' + count + 'for the word'  + list[x]

'''

escape = open('vybhav.txt')

worddic = {}

for line in escape:
 print line
 myline = line.split()
 print (myline)
