from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://malloliabhi:mongodb@cluster0.t7pzf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d={
    "name":"abhishek",
    "email":"abhi@gmail.com"
}

db=client['mongotest']
coll = db['test']
coll.insert_one(d )
