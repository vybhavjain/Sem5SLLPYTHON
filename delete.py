class person:

 __secretcount = 0;
 personCount = 0;
 def __init__(self,name,age):  #constructor because of __init__ 
  self.name = name;    # self can be replaced anytime with another word in the constructor defintion itself
  self.age = age;
  person.personCount +=1
  self.__secretcount +=1

p1 = person("suppandi",14)
p2 = person("Ramu",12)

print " \n Age is : ", person.personCount 

print " \n Age of person 2 is : ", person.__secretcount # error as secretcount is private

# del p2 or del p2.age delets specific commands

