import pymongo

URL = "mongodb://localhost:27017/"
client = pymongo.MongoClient(URL)
db = client['iShare']

# create the user login
all_users = db["allusers"]

# create the
repos = db['repos']

