class CircularBuffer:
    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._buffer = []

    def put(self, item):
        if self._size == self._capacity:
            self._buffer.pop(0)
            self._size -= 1

        self._buffer.append(item)
        self._size += 1

    def get(self):
        if self._size > 0:
            item = self._buffer.pop(0)
            self._size -= 1
            return item


if __name__ == '__main__':
    buffer = CircularBuffer(3)

    print(buffer.get() is None)  # True

    buffer.put(1)
    buffer.put(2)
    print(buffer.get() == 1)  # True

    buffer.put(3)
    buffer.put(4)
    print(buffer.get() == 2)  # True

    buffer.put(5)
    buffer.put(6)
    buffer.put(7)
    print(buffer.get() == 5)  # True
    print(buffer.get() == 6)  # True
    print(buffer.get() == 7)  # True
    print(buffer.get() is None)  # True

    buffer2 = CircularBuffer(4)

    print(buffer2.get() is None)  # True

    buffer2.put(1)
    buffer2.put(2)
    print(buffer2.get() == 1)  # True

    buffer2.put(3)
    buffer2.put(4)
    print(buffer2.get() == 2)  # True

    buffer2.put(5)
    buffer2.put(6)
    buffer2.put(7)
    print(buffer2.get() == 4)  # True
    print(buffer2.get() == 5)  # True
    print(buffer2.get() == 6)  # True
    print(buffer2.get() == 7)  # True
    print(buffer2.get() is None)  # True