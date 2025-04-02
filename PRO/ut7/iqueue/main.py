from __future__ import annotations


class IntegerQueue:
    def __init__(self, *, max_size: int = 10):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item: int) -> bool:
        if len(self.items) >= self.max_size:
            return False
        self.items.append(item)
        return True

    def dequeue(self) -> int:
        return self.items.pop(0)

    def head(self) -> int:
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) == self.max_size

    def expand(self, factor: int = 2) -> None:
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        with open(path, "w") as file:
            content = ",".join((str(num) for num in self.items))
            file.write(content)

    @classmethod
    def load_from_file(cls, path: str) -> IntegerQueue:
        result = IntegerQueue()
        file_content = open(path).readline().split(",")
        for item in file_content:
            num = int(item)
            if not result.enqueue(num):
                result.expand()
                result.enqueue(num)
        return result

    def __getitem__(self, index: int) -> int:
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        self.items[index] = item

    def __len__(self) -> int:
        return len(self.items)

    def __add__(self, other: IntegerQueue) -> IntegerQueue:
        new_size = self.max_size + other.max_size
        new_content = self.items + other.items
        result = IntegerQueue(max_size=new_size)
        result.items = new_content
        return result

    def __iter__(self) -> IntegerQueueIterator:
        return IntegerQueueIterator(self)

    def __str__(self) -> str:
        return ','.join((str(num) for num in self.items))

class IntegerQueueIterator:
    def __init__(self, queue: IntegerQueue):
        self.queue = queue
        self.pointer = 0

    def __next__(self) -> int:
        if self.pointer >= len(self.queue):
            raise StopIteration
        num = self.queue[self.pointer]
        self.pointer += 1
        return num