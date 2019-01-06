def atomicdictionary():
	atomicelements = {'H':'Hydrogen','He':'Helium','Au':'Gold','S':'Sulphur'}
	atomicelements['Li']='Lithium'
	for i in atomicelements:
		print "Key is ",i," Value is ",atomicelements[i]
	numb=len(atomicelements)
	print "origanal number of elements ",numb
	print "enter new element "
	ans='y'
	while ans=='y'or ans=='Y':
		key=raw_input("Enter the atomic symbol\t")
		value=raw_input("Enter the atomic element name\t")
		if key not in atomicelements:
			atomicelements[key]=value
			print "Inserted"
		else:
			print "Already exists in dictionary"
		ans=raw_input("Do you want more elements?(y/n or Y/N)")
	print atomicelements
	print "number of elements are ",len(atomicelements)
	search=raw_input("Enter the elemnet to be searched\t")
	if search in atomicelements:
		print "yes element %s exists" %search
		print "Its value is: %s" %atomicelements[search]
	else:
		print "element does not exist"
    
atomicdictionary()
