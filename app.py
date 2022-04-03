# 'from urllib.request import Request
# import firebase_admin
import pyrebase
from tkinter import EW
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# import cgi
# form = cgi.FieldStorage()


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

    print("u dont beleive me")
    print(email, password)
    # check database if this email/pw combo is correct
    isLoggedIn = True if email == 'hi@ucr.edu' else False

    return jsonify({"status": isLoggedIn, "groceries": ['eggs', 'fish', 'stek']})

@app.route('/add_region', methods =['POST'])
def signup():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username)
    print(request.form['email'])

    return (request.form['email'])
    
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

()