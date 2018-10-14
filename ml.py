
# K-Nearest Neighbors (K-NN)

# Importing the libraries
import pandas as pd
import requests
import smtplib

names = requests.get("https://mybmtcroute.herokuapp.com/busNumber/names") 
names_json = names.json()
name_array =(names_json['route'])



# Importing the dataset
dataset = pd.read_csv('2.csv')
X = dataset.iloc[:,:63].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

X_test_real = X[:,:]
X_test_real = sc.transform(X_test_real)

# Predicting the Test set results
y_pred = classifier.predict(X_test_real)

array_people = []


for i in range(100):
  if y_pred[i] == 1:
      print(i+2)
      array_people.append(i+2)
       
name = []      
print(array_people)       
for j in array_people:
    name.append(name_array[j])

#print (name_array) 

#for key, value in contents.items():
 #   print ( key, 'corresponds to', contents[key] )
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()


#Next, log in to the server
server.login("mylanhackathon12345@gmail.com", "vybhav123")
msg1 = "List of high priority patients!!! " + " ".join(str(x) for x in name)



print(msg1)
server.sendmail("mylanhackathon12345@gmail.com", "vybhavjain6@gmail.com ", msg1)

 # msg1.status_code = 200
