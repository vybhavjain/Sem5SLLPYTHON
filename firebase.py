from firebase import firebase
firebase = firebase.FirebaseApplication('https://farmersfriend-857c9.firebaseio.com/', None)
result = firebase.get('/Params', None)

print(result)
