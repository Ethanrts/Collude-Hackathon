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

category_string = ''
product_name = 'Almond Milk'
quantity_var = ''
# firestore_db.collection(u'Grocery_List').add({'Category': 'Dairy', 'Product Name': product_name, 'Quantity': 1})


snapshots = list(firestore_db.collection(u'Grocery_Tags').get())
for snapshot in snapshots:
    print(snapshot.to_dict())

temp = ""
temp2 = ""
count = 3

while (count > 0):
    for snapshot in snapshots:
        if (snapshot.to_dict().get('Category') != temp):
            temp = snapshot.to_dict().get('Category')
            count = count - 1
            print(snapshot.to_dict().get('Category'))

        if (count == 0):
            break

def main():
    first_header = 'testing'

    # Read the HTML file
    HTML_File=open('list.html','r')
    s = HTML_File.read().format(p=main())
    print(s)

main()

