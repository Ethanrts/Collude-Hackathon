# from urllib.request import Request
# import firebase_admin
# from firebase_admin import credentials, firestore

# import pyrebase
from tkinter import EW
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# import cgi
# form = cgi.FieldStorage()

# initialize sdk
# cred = credentials.Certificate("collude-58309-firebase-adminsdk-qd4m1-1925d38b46.json")
# firebase_admin.initialize_app(cred)
# # initialize firestore instance
# firestore_db = firestore.client()



app = Flask(__name__)
CORS(app)


# email = form.getvalue('email')
# password_ = form.getvalue('password')

# firebaseConfig = {
#   'apiKey': "AIzaSyA_QO6UfhhGyYv_HUVtOQnDqEJjPIefOGU",
#   'authDomain': "collude-58309.firebaseapp.com",
#   'projectId': "collude-58309",
#   'storageBucket': "collude-58309.appspot.com",
#   'messagingSenderId': "547641500704",
#   'appId': "1:547641500704:web:4c91263a884dd6fd960845",
#   'measurementId': "G-DMVZKWYXQN",
#   'databaseURL': ""}

# # connect to firebase acc
# firebase=pyrebase.initialize_app(firebaseConfig)

# auth=firebase.auth()

@app.route('/login')
def login():
    email = request.args.get('email')
    password = request.args.get('password')

    email_check = "aalsu013@ucr.edu"
    password_check = "testing"

    # if(email == email_check and password == password_check):
      
    #   list_page()
    
    # else:
      #html display try again 

    #print(email, password)
    # check database if this email/pw combo is correct
    isLoggedIn = True if (email == email_check and password == password_check) else False
     

    return jsonify({"status": isLoggedIn, "groceries": ['eggs', 'fish', 'stek']})

    #return jsonify({"status": isLoggedIn, ## here })


@app.route('/list')
def list_page():
  ## add items to database
  ## front end needs to create tags for each product name and its category 
    ## if we create tags, clicking on them will add them to the list .. so we may just drop quantities altogether ... 
    ## 

  category_string = ''
  product_name = 'Almond Milk'
  quantity_var = ''
  #firestore_db.collection(u'Grocery_Tags').add({'Category': 'Dairy', 'Product Name': product_name})

#   snapshots = list(firestore_db.collection(u'Grocery_Tags').get())
  for snapshot in snapshots:
    print(snapshot.to_dict())

@app.route('/sign_up')
def signup():
    email = request.args.get('email')
    password = request.args.get('password')
    password2 = request.args.get('password2')
    isLoggedIn = True if (password == password2) else False
   
    ## after signing up, display some sort of success screen -- html 
    ## go striaght to the list_page / grocery list web page 
    return jsonify({"status": isLoggedIn}) 
    
    print(password)
    #return jsonify({"content": True if username == "ryan" else False })
    # return jsonify({"content": True if (username,password) == auth.sign_in_with_email_andpassword(email, password_) else False})
#   email=input("Enter Email: ")
#   password=input("Enter Password: ")
#   try:

#     return app.send_static_file("index.html")
#     user=auth.create_user_with_email_andpassword(email_,password_)
#     print("Success")
#   except:
#     print("TRY AGAIN")


# localhost:500/login
# @app.route("/login")
# def login():
#   email = input("Enter Email: ")
#   password = input("Enter Password: ")
#   try:
#     # user = auth.sign_in_with_email_andpassword(email, password_)
#     print("Success")
#   except:
#     print("TRY AGAIN")

# login()

# if __name__ == '__main__':
#     app.run()

#only here for adding the gorcery tags below