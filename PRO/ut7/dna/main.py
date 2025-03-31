from __future__ import annotations


class DNA:
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'
    BASES_ORDER = (ADENINE, CYTOSINE, GUANINE, THYMINE)

    def __init__(self, sequence: str):
        self.sequence = sequence

    def __str__(self):
        return f'{self.sequence}'

    @property
    def adenines(self) -> int:
        return self.sequence.count(DNA.ADENINE)

    @property
    def cytosines(self) -> int:
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def guanines(self) -> int:
        return self.sequence.count(DNA.GUANINE)

    @property
    def thymines(self) -> int:
        return self.sequence.count(DNA.THYMINE)

    def __add__(self, other: DNA) -> DNA:
        result = ''
        if len(self.sequence) > len(other.sequence):
            longer_sequence = self.sequence
            shorter_sequence = other.sequence
        else:
            longer_sequence = other.sequence
            shorter_sequence = self.sequence
        for base_a, base_b in zip(self.sequence, other.sequence):
            result += (
                base_a if DNA.BASES_ORDER.index(base_a) >= DNA.BASES_ORDER.index(base_b) else base_b
            )
        result += longer_sequence[len(shorter_sequence) :]
        return DNA(result)

    def __len__(self):
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        return {
            'A': (self.adenines / len(self.sequence)) * 100,
            'C': (self.cytosines / len(self.sequence)) * 100,
            'G': (self.guanines / len(self.sequence)) * 100,
            'T': (self.thymines / len(self.sequence)) * 100,
        }

    def __mul__(self, other: DNA) -> DNA:
        new_sequence = ''.join(
            (base for base, other_base in zip(self.sequence, other.sequence) if base == other_base)
        )
        return DNA(new_sequence)

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        file_content = open(path).readline()
        return DNA(file_content)

    def dump_to_file(self, path: str) -> None:
        with open(path, "w") as file:
            file.write(f'{self.sequence}')

    def __getitem__(self, index: int) -> str:
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        valid_bases = ('A', 'C', 'G', 'T')
        if base not in valid_bases :
            base = DNA.ADENINE
        new_sequence = self.sequence[:index] + base + self.sequence[index:]
        self.sequence = new_sequence