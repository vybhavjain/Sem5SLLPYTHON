w = []
s = []

with open("1.txt") as f:
    for line in f:
        for word in line.split():
            w.append(word)
            
s = w[::-1]

a = open("3.txt","wb") 
a.close()

with open("3.txt", "w+") as t:
    for x in s:
        t.write(x + "\n")
