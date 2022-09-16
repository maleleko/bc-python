


class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.petnoise = noise

    def sleep(self):
        print(f"{self.name} is feeling sleepy. It's going to take a nap.")
        print(" ")
        print("*zZz*")
        print(" ")
        self.energy += 25
        print(f"{self.name} is feeling well rested. Energy went up 25! Energy is now: {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health +=10
        print(f"{self.name} ate good! They're super satisfied. They just belched!")
        return self

    def play(self):
        print(f"{self.name} had a lot of fun! They exerted a lot of energy.")
        self.energy -= 15
        print(f"{self.name} grew a little stronger! Health is now {self.health}")
        self.health += 5
        return self


    def noise(self):
        print(f'{self.name} is happy. {self.name} speaks with joy! {self.name} says: "{self.petnoise}"') 
        return self

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

charmander = Pet("Charmander", "baby fire dragon", "fire dance", "ayooo a-hah")
treats = "fire gummies"
pet_food = "spicy flaming pasta"
maleko = Ninja("Koh", "Ozbe", charmander, treats, pet_food)


maleko.feed()
print("--------------------")
maleko.walk()
print("--------------------")
maleko.bathe()
print("--------------------")
charmander.sleep()

