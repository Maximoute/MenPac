# oop = object oriented programigne
class animal:
	def __init__(self,race,sexe,age,couleur="bleu"):
		self.race = race
		self.sexe = sexe
		self.age = age
		self.couleur = couleur

	def viellir(self):
		self.age = self.age + 1 

race = "chien"
sexe = "F"
age = 2

chat = animal("chat","M","10")
zoo = []
for i in range(10):
	if i%2 == 0:
		chienn = animal("chien",sexe,age,"blanc")
	else:
		chienn = animal("chien",sexe,age,"noir")

	zoo.append(chienn)

print(f"{zoo[4].age} ans")
zoo[4].viellir()
print(zoo[4].age)