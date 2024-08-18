class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed


if __name__ == '__main__':
    a = Dog("Golden Retriever")
    b = Dog("Poodle")

