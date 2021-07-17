class Animals():
	'''Main class Animal'''
	def __init__(self,category,name,legs,teritory):
		self.classification = category
		self.name = name
		self.noflegs = legs
		self.teritory = teritory
	def __str__(self):
		print(f"This animal in '{self.classification}' group, It stays on {self.teritory}. It has {self.noflegs}. Its name is {self.name}")

# Class inheritance inherits from animal above 
class Sheep(Animals):
	'''Class inheritance'''
	def __init__(self, category, name, legs, teritory,skincover):
		super().__init__(category, name, legs, teritory)
		self.skin = skincover

# This is a dunder/special/magic method
	def __str__(self):
	    print(f"{self.classification} {self.name} {self.noflegs} {self.teritory} {self.skin}")
	
	# This is a private method
	def __private(self):
		print(f"{self.name}You managed to call a private method from class inheritance")

an1 = Animals("Omnivorous","Cow",4,"land")
an2 = Animals("Canivorous","Crocodile",4,"Land & water")
print(an1.__str__())
print(an2.teritory)

sheep1 = Sheep("Home-animal", "Sheep",4,"Land","Cotton")

print(issubclass(Sheep,Animals))
print(isinstance(sheep1,Sheep))
print(sheep1.__str__())
print("Calling a private method on an instance of the sublass on below instance of Sheep")
# How to call a private method
print(sheep1._Sheep__private())

# function with args and Kwargs
def Argskwargs(*args,**kwargs):
	print(args,kwargs)

students = ["Robert","Ferdinant","Duncan","Walace","Vinod"]
studentsRecods = {"Robert":{"Maths":"89%","English":"84%","Kiswahili":"77%"},"Ferdinant":{"Maths":"78%","English":"66%","Kiswahili":"64%"},"Duncan":{"Maths":"74%","English":"71%","Kiswahli":"98%"}}

# function, args positional
print("Args positional")
Argskwargs(students)

# function, args positional, no kwargs positonal printed despite inputing dictionary
print("NKwargs positional left empty despite passing ing a dectionary(key value pair")
Argskwargs(students,studentsRecods)

print("Now prints args in its position and kwargs in its position")
Argskwargs(*students,**studentsRecods)


with open("Records.txt","w") as fr:
	record = fr.write(str(studentsRecods))
with open("beststudents.txt", "a") as fb:
	best = fb.write(f"\n{str(students)}\n{str(studentsRecods)}")
	

with open("Records.txt","r") as fi:
	gradesStudents = fi.read()
	print(gradesStudents)