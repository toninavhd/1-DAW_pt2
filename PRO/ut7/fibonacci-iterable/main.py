class Fibonacci:
    def __init__(self, n: int):
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        for _ in range(self.n):
            yield self.a
            self.a, self.b = self.b, self.a + self.b

    

    
def run(n: int) -> list[int]:
    return list(Fibonacci(n))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
