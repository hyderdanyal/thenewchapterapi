import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

data=[]
cred = credentials.Certificate('book-cred.json')
firebase_admin.initialize_app(cred)
def bookid(name,uid):
  # Use a service account

  db = firestore.client()



  # name='danyal hyder'
  # uid='ATKABiBicvcuRZvoqkqO4Ru8gDW2'
  # Add a new doc in collection 'cities' with ID 'LA'
  doc_ref=db.collection(u'mylist').document(name).collection(uid).stream()
  for doc in doc_ref:
      data.append(doc.id)
      # print(u'{} => {}'.format(doc.id, doc.to_dict()))
  return data    
def returndata():
  return data
  
