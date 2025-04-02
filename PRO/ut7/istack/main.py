from __future__ import annotations


class IntegerStack:

    def __init__(self, *, max_size: int = 10):
        self.max_size = max_size
        self.items = []

    def push(self, item: int) -> bool:
        if len(self.items) >= self.max_size:
            return False
        self.items.insert(0, item)
        return True

    def pop(self) -> int:
        return self.items.pop(0)

    def top(self) -> int:
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) == self.max_size

    def expand(self, factor: int = 2) -> None:
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write('\n'.join(str(item) for item in self.items))

    @classmethod
    def load_from_file(cls, path: str) -> IntegerStack:
        result = IntegerStack()
        for line in reversed(open(path).readlines()):
            num = int(line.strip())
            if not result.push(num):
                result.expand()
                result.push(num)
        return result

    def __getitem__(self, index: int) -> int:
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        self.items[index] = item

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return '\n'.join(map(str, self.items))

    def __add__(self, other: IntegerStack) -> IntegerStack:
        result = IntegerStack(max_size=self.max_size + other.max_size)
        result.items = other.items + self.items
        return result

    def __iter__(self) -> IntegerStackIterator:
        return IntegerStackIterator(self)


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        self.stack = stack
        self.pointer = 0

    def __next__(self) -> int:
        if self.pointer >= len(self.stack):
            raise StopIteration
        num = self.stack[self.pointer]
        self.pointer += 1
        return num