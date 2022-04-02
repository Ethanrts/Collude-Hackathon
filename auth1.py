import firebase_admin
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyA_QO6UfhhGyYv_HUVtOQnDqEJjPIefOGU",
  'authDomain': "collude-58309.firebaseapp.com",
  'projectId': "collude-58309",
  'storageBucket': "collude-58309.appspot.com",
  'messagingSenderId': "547641500704",
  'appId': "1:547641500704:web:4c91263a884dd6fd960845",
  'measurementId': "G-DMVZKWYXQN",
  'databaseURL': ""}

#connect to firebase acc
firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

def signup():
  email=input("Enter Email: ")
  password=input("Enter Password: ")
  try:

    user=auth.create_user_with_email_and_password(email,password)
    print("Success")
  except:
    print("TRY AGAIN")

def login():
  email = input("Enter Email: ")
  password = input("Enter Password: ")
  try:
    user = auth.sign_in_with_email_and_password(email, password)
    print("Success")
  except:
    print("TRY AGAIN")

ans=input("New user? y/n")

if ans == 'y':
  signup()

elif ans== 'n':
  login()