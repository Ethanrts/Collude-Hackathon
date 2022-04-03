from creaet_db import my_func

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

   return jsonify(my_func())


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
    #