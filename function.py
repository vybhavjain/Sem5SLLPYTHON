def atomic():
 atomic_mass = {
'H': 1,
'He': 4,
'Li': 6,
'O': 16,
'F': 19,
'C': 12,
'S': 32
}
 atomic_mass['Cu']=65

 numb=len(atomic_mass)
 print " Total number of elements are : ",numb
 answer = "y"

 while answer == "y":
  key=raw_input("Enter the atomic symbol: \t")
  value=raw_input("Enter the atomic mass: \t")
  atomic_mass[key] = value
  answer = raw_input("Enter y for one more new element or n for no")

 print(atomic_mass) 
 numb=len(atomic_mass)
 print " Total number of elements are : ",numb

