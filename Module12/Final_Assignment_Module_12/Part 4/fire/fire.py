# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://assignment-module12-f6d31-default-rtdb.firebaseio.com/'
})

# save data
ref = db.reference('database/')
pres_ref = ref.child('presidents')
pres_ref.set({
    'first': {
        'date_of_birth': 'February 22, 1732',
        'full_name': 'George Washington'
    },
    'second': {
        'date_of_birth': 'October 30, 1735',
        'full_name': 'John Adams'
    }
})

# update data
hopper_ref = pres_ref.child('second')
hopper_ref.update({
    'occupation': 'Attorney'
})

# read data
handle = db.reference('database/presidents/first')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())