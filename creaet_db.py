import firebase_admin
from firebase_admin import credentials, firestore

# initialize sdk
cred = credentials.Certificate("collude-58309-firebase-adminsdk-qd4m1-1925d38b46.json")
firebase_admin.initialize_app(cred)
# initialize firestore instance
firestore_db = firestore.client()
# add data

# firestore_db.collection(u'Grocery_List').add({'Category': 'Dairy', 'Product Name': product_name, 'Quantity': 1})


# snapshots = list(firestore_db.collection(u'Grocery_Tags').get())
# for snapshot in snapshots:
#     print(snapshot.to_dict())

temp = ""
temp2 = ""
count = 3

def my_func():
    veg_cat = {}
    for snapshot in snapshots:
        category = str(snapshot.to_dict().get('Category'))
        pname = str(snapshot.to_dict().get('Product Name'))
        #print(veg_cat.get('Category') is None)
        if veg_cat.get(category) is None:
            veg_cat[category] = [pname]

        else:
            #print(veg_cat[category])
            veg_cat[category].append(pname)

        # if (snapshot.to_dict().get('Category') != temp):
        #     temp = snapshot.to_dict().get('Category')
        #     # count = count - 1
        #
        #     if temp == 'Vegetables':
        #         key = snapshot.to_dict().get('Category')
        #         veg_cat[key] = snapshot.to_dict().get('Product Name')
        #     print(snapshot.to_dict().get('Category'))
        #

    # veg_cat = {"Vegetables": ["Celery", "Asparagus", "Corn", "Cabbage", "Spinach", "Squash"] , "Protein": ["A5 Wagyu", "Salmon", "Pork", "Ground Beef", "Chicken"] ,"Dairy": ["2% Milk", "Almond Milk", "Goat Milk"]}
    
    return veg_cat 


