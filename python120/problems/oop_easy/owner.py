class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []

    @property
    def name(self):
        return self._name

    @property
    def pets(self):
        return self._pets

    def adopt(self, pet):
        self._pets.append(pet)

    def number_of_pets(self):
        return len(self._pets)
