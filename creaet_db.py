import firebase_admin
from firebase_admin import credentials, firestore


# initialize sdk
cred = credentials.Certificate("collude-58309-firebase-adminsdk-qd4m1-1925d38b46.json")
firebase_admin.initialize_app(cred)
# initialize firestore instance
firestore_db = firestore.client()
# add data
#firestore_db.collection(u'List').add({'Category': 'Dairy', 'Product Name': '2% Milk', 'Quantity': 2})
# read data
snapshots = list(firestore_db.collection(u'Grocery_List').get())
for snapshot in snapshots:
    print(snapshot.to_dict())