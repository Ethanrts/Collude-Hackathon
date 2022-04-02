import firebase_admin
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyA_QO6UfhhGyYv_HUVtOQnDqEJjPIefOGU",
  'authDomain': "collude-58309.firebaseapp.com",
  'projectId': "collude-58309",
  'storageBucket': "collude-58309.appspot.com",
  'messagingSenderId': "547641500704",
  'appId': "1:547641500704:web:4c91263a884dd6fd960845",
  'measurementId': "G-DMVZKWYXQN"}

#connect to firebase acc
firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

