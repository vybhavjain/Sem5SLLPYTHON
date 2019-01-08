class Student:		
	def __init__(self,name,age,marks):
		self.name=name
		self.age=age
		self.marks=marks
	
	def  accept():
		l=[]
		n=input("Enter name of student")
		a=input("Enter age")
		for i in range(3):
			x=int(input("Enter marks of sub " + str(i+1)))
			l.append(x)
		s=Student(n,a,l)
		return s
	
	def display(self):
		print("Name :" + self.name)
		print("Age :" + str(self.age))
		print("List of marks :" + str(self.marks))
    
    
s1=Student('vybhav',15,[92,70,82])
s1.display()
s2=Student.accept()
s2.display()
