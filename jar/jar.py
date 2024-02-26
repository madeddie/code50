class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError

        self.capval = capacity
        self.sizeval = 0

    def __str__(self):
        return "🍪" * self.sizeval

    def deposit(self, n):
        if (self.sizeval + n) > self.capval:
            raise ValueError

        self.sizeval += n

    def withdraw(self, n):
        if (self.sizeval - n) < 0:
            raise ValueError
        self.sizeval -= n

    @property
    def capacity(self):
        return self.capval

    @property
    def size(self):
        return self.sizeval

def main():
    jar = Jar(capacity=15)

if __name__ == "__main__":
    main()
