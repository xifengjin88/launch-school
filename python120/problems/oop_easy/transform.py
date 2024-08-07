class Transform:
    def __init__(self, s):
        self.s = s

    def uppercase(self):
        return self.s.upper()

    @staticmethod
    def lowercase(s):
        return s.lower()

    
if __name__ == '__main__':
    my_data = Transform('abc')
    print(my_data.uppercase())  # ABC
    print(Transform.lowercase('XYZ'))  # xyz
