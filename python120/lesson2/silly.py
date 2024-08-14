class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def _is_numeric(self, value):
        if isinstance(value, int):
            return True
        return value.isdigit()

    def __add__(self, other):
        if (not isinstance(other, str)) and (not isinstance(other, int)):
            return NotImplemented

        if self._is_numeric(self.value) and self._is_numeric(other):
            return Silly(int(self.value) + int(other))
        return Silly(str(self.value) + str(other))

if __name__ == '__main__':
    print(Silly('abc') + 'def')  # Silly('abcdef')
    print(Silly('abc') + 123)  # Silly('abc123')
    print(Silly(123) + 'xyz')  # Silly('123xyz')
    print(Silly('333') + 123)  # Silly(456)
    print(Silly(123) + '222')  # Silly(345)
    print(Silly(123) + 456)  # Silly(579)
    print(Silly('123') + '456')  # Silly(579)
