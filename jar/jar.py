class Jar:
    def __init__(self, capacity=12):
        elif int(capacity) < 0:
            raise ValueError

        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.capacity

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError

        self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError

        self.size -= n

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size

def main():
    jar = Jar(capacity=15)

if __name__ == "__main__":
    main()
