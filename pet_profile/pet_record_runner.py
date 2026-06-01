from pet_record import Pet

def main():
    name = input("Enter your pet's name: ")
    animal_type = input("Enter your pet's type: ")
    age = int(input("Enter your pet's age: "))

    pet = Pet()
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    print("\nPet Details:")
    print("Name:", pet.get_name())
    print("Type:", pet.get_animal_type())
    print("Age:", pet.get_age())