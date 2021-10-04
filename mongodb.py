# DATABASE CONNECTION
# THIS MODULE CREATE A CONNECTION WITH MONGO DATABASE 
import pymongo



class MongoDBHandler:
	def __init__(self, PASSWORD, DATABASE, COLLECTION):
		# self.connection_str = "mongodb+srv://MongoBDA-R:" + PASSWORD + "@proyecto1bda-nodor.yfva8.mongodb.net/" + DATABASE + "?retryWrites=true&w=majority"
		self.connection_str = "mongodb+srv://MongoBDA-R:"+ PASSWORD +"@proyecto1bda-nodor.yfva8.mongodb.net/Nodo_R"
		self.client_mongodb = pymongo.MongoClient(connection_str, serverSelectionTimeoutMS=5000)
		self.database = self.client_mongodb[DATABASE]
		self.collection = self.database[COLLECTION]
		self.password = PASSWORD


	# GET ALL DATA FROM DATABASE 
	def readAllFromMongoDB(self):
		try:
			result = []
			for data in self.collection.find({}, {'_id': False}):
				result.append(data)
			return result
		except Exception:
			print("* Unable to connect to server.")
			return None


	# GET THE FIRST RECORD THAT MATCH WITH CONDITION
	def readOneFromMongoDB(self, filter_attrib, value_attrib):
		try:
			# print(filter_attrib)
			result = self.collection.find_one({filter_attrib: value_attrib}, {'_id': False})
			return result
		except Exception:
			print("* Unable to connect to server.")
			return None


	# RETURN EACH OCURRENCE THAT MATCHES THE CONDITION
	def readMultiFromMongoDB(self, filter_attrib, value_attrib):
		try:
			result = []
			for data in self.collection.find({filter_attrib: value_attrib}, {'_id': False}):
				result.append(data)
			return result
		except Exception:
			print("* Unable to connect to server.")
			return None


	# INSERT ONE ENTRY INTO MONGODB
	def insertToMongoDB(self, new_entry):
		try:
			self.collection.insert_one(new_entry)
			return 0
		except Exception:
			print("* Unable to connect to server.")
			return None


	# UPDATE VALUES FOR DOCUMENTS MATCHING A CONDITION
	def updateToMongoDB(self, update_attribute, update_value, new_value):
		try:
			query = {update_attribute : update_value}
			set_new_values = { "$set": new_value }
			self.collection.update_many(query, set_new_values)
			return 0
		except Exception:
			print("* Unable to connect to server.")
			return None


	# DELETE ONE RECORD THAT MATCH A CONDITION
	def deleteToMongoDB(self, delete_attribute, delete_value):
		try:
			self.collection.delete_one({delete_attribute : delete_value})
			return 0
		except Exception:
			print("* Unable to connect to server.")
			return None




##########################################################################################################################
######################################### - Instance Constant Values - ###################################################
##########################################################################################################################
PASSWORD = "MongoDBA-R"
# DATABASE = "BDA"
DATABASE = "Nodo_R"
# COLLECTION = "Lab2_BDA"
COLLECTION = "Employees"
connection_str = "mongodb+srv://MongoBDA-R:"+PASSWORD+"@proyecto1bda-nodor.yfva8.mongodb.net/Nodo_R"
# connection_str = "mongodb+srv://MongoBDA-R:" + PASSWORD + "@proyecto1bda-nodor.yfva8.mongodb.net/" + DATABASE + "?retryWrites=true&w=majority"
# connection_str = 'mongodb://Fallas:fallas123@cluster0-shard-00-00.ctzqs.mongodb.net:27017,cluster0-shard-00-01.ctzqs.mongodb.net:27017,cluster0-shard-00-02.ctzqs.mongodb.net:27017/BDMultimedia?ssl=true&replicaSet=atlas-ls6q9y-shard-0&authSource=admin&retryWrites=true&w=majority'
# connection_str = "mongodb+srv://Fallas:fallas123@cluster0.ctzqs.mongodb.net/Proyecto1BDA?retryWrites=true&w=majority"
##########################################################################################################################

# test = MongoDBHandler("MongoDBA-R", "Nodo_R", "Employees")
# test = MongoDBHandler("MongoDBA-R", "BDA", "Lab2_BDA")
# print(test.readAllFromMongoDB())
# print(test.readOneFromMongoDB('email', 'email14@domain.com'))
# print(test.readMultiFromMongoDB("ti_area", True))
# print(test.insertToMongoDB({"Name": "Gerudo Valley", "Author": "Saria", "User Rating": 5, "Reviews": 17350, "Price": 11, "Year": 1996,"Genre": "Fiction"}))
# print(test.updateToMongoDB("Name", "Gerudo Valley", { "Author": "Zelda", "Price": 20}))
# print(test.deleteToMongoDB("Name", "Gerudo Valley"))