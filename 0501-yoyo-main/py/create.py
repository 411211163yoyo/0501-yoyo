import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "周攸晨",
  "mail": "mojeef2012@gmail.com",
  "lab": 411211189
}

doc_ref = db.collection("靜宜資管").document("Jian")
doc_ref.set(doc)
