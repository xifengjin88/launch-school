class Student:
    school_name = "Oxford"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name


if __name__ == "__main__":
    print(Student.school_name)
    print(Student.get_school_name())
