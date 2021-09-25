# DATABASE CONNECTION
# THIS MODULE CREATE A CONNECTION WITH MONGO DATABASE 
import pymongo

PASSWORD = "MongoDBA-R"
DATABASE = "BDA"
COLLECTION = "Lab2_BDA"

connection_str = "mongodb+srv://MongoBDA-R:" + PASSWORD + "@proyecto1bda-nodor.yfva8.mongodb.net/" + DATABASE + "?retryWrites=true&w=majority"


# try:
# 	client_mongodb = pymongo.MongoClient(connection_str, serverSelectionTimeoutMS=5000)
# 	# database = client_mongodb[DATABASE]
# 	# collection = database[COLLECTION]
# 	# for data in collection.find():
# 	# 	print(data)
# 	# print(client_mongodb.server_info())
# 	readFromMongo()
# 	print(0)
# except Exception:
# 	print("Unable to connect to server.")




class MongoDBHandler:
	def __init__(self, PASSWORD, DATABASE, COLLECTION):
		self.password = PASSWORD
		self.database = DATABASE
		self.collection = COLLECTION
		self.connection_str = "mongodb+srv://MongoBDA-R:" + PASSWORD + "@proyecto1bda-nodor.yfva8.mongodb.net/" + DATABASE + "?retryWrites=true&w=majority"
		self.client_mongodb = pymongo.MongoClient(connection_str, serverSelectionTimeoutMS=5000)

	# GET ALL DATA FROM DATABASE 
	def readAllFromMongoDB(self):
		try:
			database_itc = self.client_mongodb[self.database]
			collection_itc = database_itc[self.collection]
			for data in collection_itc.find():
				print(data)

		except Exception:
			print("Unable to connect to server.")


	# GET THE FIRST RECORD THAT MATCH WITH CONDITION
	def readOneFromMongoDB(self, filter_attrib, value_attrib):
		database_itc = self.client_mongodb[self.database]
		collection_itc = database_itc[self.collection]
		result = collection_itc.find_one({filter_attrib: value_attrib})
		print(result)

	# RETURN EVERY APARISON OF MATCH CONDITION
	def readMultiFromMongoDB(self, filter_attrib, value_attrib):
		database_itc = self.client_mongodb[self.database]
		collection_itc = database_itc[self.collection]
		result = collection_itc.find({filter_attrib: value_attrib})
		for data in result:
			print(data)

	# INSERT ONE ENTRY INTO MONGODB
	def insertToMongoDB(self, new_entry):
		database_itc = self.client_mongodb[self.database]
		collection_itc = database_itc[self.collection]
		collection_itc.insert_one(new_entry)

	# UPDATE VALUES FOR DOCUMENTS MATCHING A CONDITION
	def updateToMongoDB(self, query, new_value):
		database_itc = self.client_mongodb[self.database]
		collection_itc = database_itc[self.collection]
		set_new_values = { "$set": new_value }
		collection_itc.update_many(query, set_new_values)

	# DELETE ONE RECORD THAT MATCH A CONDITION
	def deleteToMongoDB(self, delete_query):
		database_itc = self.client_mongodb[self.database]
		collection_itc = database_itc[self.collection]
		collection_itc.delete_one(delete_query)







# test = MongoDBHandler("MongoDBA-R", "BDA", "Lab2_BDA")
# test.readAllFromMongoDB()
# test.readOneFromMongoDB("Author", "Stephen King")
# test.readMultiFromMongoDB("Author", "Stephen King")
# test.insertToMongoDB({"Name": "Gerudo Valley", "Author": "Saria", "User Rating": 5, "Reviews": 17350, "Price": 11, "Year": 1996,"Genre": "Fiction"})
# test.updateToMongoDB({ "Name": "Gerudo Valley" }, { "Author": "Saria", "Price": 20})
# test.deleteToMongoDB({ "Name": "Gerudo Valley" })