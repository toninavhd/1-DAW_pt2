class Fibonacci:
    def __init__(self, n: int):
        self.n = n
        self.a = 0
        self.b = 1
        self.pointer = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pointer >= self.n:
            raise StopIteration
        else:
            f_value = self.a
            self.a, self.b = self.b , self.a + self.b
            self.pointer += 1
            return f_value

    
def run(n: int) -> list[int]:
    return list(Fibonacci(n))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
