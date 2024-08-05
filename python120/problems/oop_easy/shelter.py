from pet import Pet
from owner import Owner


class Shelter:
    def __init__(self):
        self._adopters = {}

    def adopt(self, owner, pet):
        if owner.name in self._adopters:
            target_owner = self._adopters[owner.name]
            target_owner.adopt(pet)
        else:
            owner.adopt(pet)
            self._adopters[owner.name] = owner

    def print_adoptions(self):
        for name, owner in self._adopters.items():
            print(f"{name} has adopted following pets:")
            for pet in owner.pets:
                print(f"a {pet.pet_type} named {pet.name}")


if __name__ == '__main__':
    cocoa = Pet('cat', 'Cocoa')
    cheddar = Pet('cat', 'Cheddar')
    darwin = Pet('bearded dragon', 'Darwin')
    kennedy = Pet('dog', 'Kennedy')
    sweetie = Pet('parakeet', 'Sweetie Pie')
    molly = Pet('dog', 'Molly')
    chester = Pet('fish', 'Chester')

    phanson = Owner('P Hanson')
    bholmes = Owner('B Holmes')

    shelter = Shelter()
    shelter.adopt(phanson, cocoa)
    shelter.adopt(phanson, cheddar)
    shelter.adopt(phanson, darwin)
    shelter.adopt(bholmes, kennedy)
    shelter.adopt(bholmes, sweetie)
    shelter.adopt(bholmes, molly)
    shelter.adopt(bholmes, chester)

    shelter.print_adoptions()
    print(f"{phanson.name} has {phanson.number_of_pets()} "
          "adopted pets.")
    print(f"{bholmes.name} has {bholmes.number_of_pets()} "
          "adopted pets.")
