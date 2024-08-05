class Pet:
    def __init__(self, pet_type, name):
        self._pet_type = pet_type
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def pet_type(self):
        return self._pet_type
