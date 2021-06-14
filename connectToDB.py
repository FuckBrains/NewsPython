import urllib
import urllib.parse
import pymongo



from pymongo import MongoClient





mongo_uri = "mongodb://monk0062006:" +  urllib.parse.quote_plus('Password@123') + "@cluster0.nbng4.mongodb.net/" +"test?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)

#client = pymongo.MongoClient(mongo_uri)


mydb = client['test']
col = mydb["test"]

post ={"_id" : 0, "name":"tim","score":"5"}
col.insert_one(post)







