
# email: Correo electronico (sera el usuario para login)
# password: Clave de acceso
# full_name: Nombre completo
# country: Pais de residencia
# university_degree: Títulos universitarios que posee (debe permitir registrar 1 o más, según lo requiera el usuario)
# programming_languages: Si es una persona del área de Tecnología de Información, se le debe consultar: o Lenguajes de programación que conoce (debe permitir registrar 1 o más, según lo requiera el usuario)
# languages: Idiomas -> debe permitir registrar 1 o más, y para cada uno indicar el nivel (básico, intermedio, avanzado)


# CLASS CREATED TO MODEL STRUCTURE FOR INSERTION TO MONGODB
class Persona:
	def __init__(self, email, password, full_name, country, university_degree, programming_languages, languages):
		self.email = email
		self.password = password
		self.full_name = full_name
		self.country = country
		self.university_degree = university_degree
		self.programming_languages = programming_languages
		self.languages = languages

# test.insertToMongoDB({"Name": "Gerudo Valley", "Author": "Saria", "User Rating": 5, "Reviews": 17350, "Price": 11, "Year": 1996,"Genre": "Fiction"})

	def createDocument(self):
		document = {}
		if (not(self.email == None)):
			document.update({'Email': self.email})
		
		if (not(self.password == None)):
			document.update({'Password': self.password})
		
		if (not(self.full_name == None)):
			document.update({'Full_name': self.full_name})
		
		if (not(self.country == None)):
			document.update({'Country': self.country})
		
		if (not((self.university_degree == []) or (self.university_degree == None))):
			document.update({'University_Degree': self.university_degree})
		
		if (not((self.programming_languages == []) or (self.programming_languages == None))):
			document.update({'Programming_Languages': self.programming_languages})
		
		if (not((self.languages == []) or (self.languages == None))):
			document.update({'Languages': self.languages})

		else:
			return None
		
		return document



# ronny = Persona("ronnyjosv259@outlook.es", "12345678", "Ronny Santamaria Vargas", "Costa Rica", ["Lic", "Phd"], ["Python", "C++"], ["English", "Spanish", "Klingon"])
# print(ronny.createDocument())