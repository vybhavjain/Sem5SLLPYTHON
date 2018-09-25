escape = open('vybhav.txt')

worddic = {}

for line in escape:
 print line
 myline = line.split()
 
 print myline

 for word in myline:
	w = worddic.get(word,0)
	print "the word %s occurs in dictionary %d times" %(word,w)

	worddic[word] = w + 1
	print "after adding the new word read is %s" %word
	print "the word %s occurs %d times in dictionary " %(word, worddic[word])

print "/n" , worddic ,"/n"


search = raw_input("Enter search string :")
if search in worddic:
 print 'found word %s %d times' %(search, worddic[search])
else:
 print 'sorry not found!'
