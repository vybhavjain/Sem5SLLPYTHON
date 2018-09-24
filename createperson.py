# or can also be :

class person:
 def __init__(self,name,age):  #constructor because of __init__ 
  self.name = name;    # self can be replaced anytime with another word in the constructor defintion itself
  self.age = age;

p1 = person("suppandi",14)
p2 = person("Ramu",12)

print " \n Name of person 1 is : ", p1.name
print " \n Age of person 1 is : ", p1.age

print " \n Name of person 2 is : ", p2.name
print " \n Age of person 2 is : ", p2.age

p2.age = 10

print " \n Age of person 2 is : ", p2.age


"""  multicomment line 
 
class person:
 def __init__(vybhav,name,age):  #constructor because of __init__ 
  vybhav.name = name;
  vybhav.age = age;

p1 = person("suppandi",14)
p2 = person("Ramu",12)

print " \n Name of person 1 is : ", p1.name
print " \n Age of person 1 is : ", p1.age

print " \n Name of person 2 is : ", p2.name
print " \n Age of person 2 is : ", p2.age

p2.age = 10

print " \n Age of person 2 is : ", p2.age


"""

