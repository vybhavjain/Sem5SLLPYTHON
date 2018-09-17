dict1 = {
   'Name1': 'Archie',
   'Age1': 17,
   'Identity1': 'Student';
}

dict2 = {
   'Name2': 'Weatherbee',
   'Age2': 52,
   'Identity2': 'Principal';
}

dict3 = {
   'Name3': 'Grundy',
   'Age3': 51,
   'Identity3': 'Teacher';
}

dict4 = dict(list(dict1.items()) + list(dict2.items()) + list(dict3.items()))

print (dict4)

dict1['name1']="Veronica"

dict4 = dict(list(dict1.items()) + list(dict2.items()) + list(dict3.items()))

print (dict4)

dict5 = {
	'Reverable' = 'no clue ' ,
	'comic' = 'old one'
}

dict6 = dict(list(dict4.items()) + list(dict5.items()))
