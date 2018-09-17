# Create a dictionary of atomic elements.
# create a list which contains the freuency of occurence of each atomic element

atomic_mass = {
'H': 1,
'He': 4,
'Li': 6,
'O': 16,
'C': 12,
'C': 12,
'F': 19,
'C': 12,
'S': 16,
'C': 12,
'S': 32
}

#print(atomic_mass)

atomic=[
('H', 1),
('He', 4),
('Li', 6),
('O',16),
('C', 12),
('C', 12),
('F', 19),
('C', 12),
('S', 16),
('C', 12),
('S', 32)
]
#print(atomic)

#from collections import Counter
#Counter(atom[0] for atom in atomic)


#c = Counter(atom[0] for atom in atomic)
#sum(v for k, v in c.iteritems() if v > 1)


d = {}
for x, y in atomic:
        d[x] = d.get(x, 0) + 1
print d
