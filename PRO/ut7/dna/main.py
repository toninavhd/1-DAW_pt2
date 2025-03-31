class DNA:
    def __init__(self,sequence:str):
        self.sequence = sequence
        adenine = 'A'
        timine = 'T'
        guanine = 'G'
        citosine = 'C'

    def __len__(self) -> int:
        seq_len = len(self.sequence)
        return seq_len
    
    def __str__(self) -> str:
        return print(self.sequence)
    
    @property
    def adenines(self)-> int:
        return self.sequence.count('A')
    
    @property
    def cytosines(self) -> int:
        return self.sequence.count('C')
    
    @property
    def guanines(self) -> int:
        return self.sequence.count('G')
    
    @property
    def thymines(self) -> int:
        return self.sequence.count('T')
    
    def __add__(self, other:DNA) -> DNA:
        new_sequence = self * other.sequence

    def stats(self) -> dict[str,float]:
        self.stats['A'] = self.adenines / len(self.sequence)
        self.stats['C'] = self.cytosines / len(self.sequence)
        self.stats['G'] = self.guanines /  len(self.sequence)
        self.stats['T'] = self.thymines / len(self.sequence)
        return self.stats
    
    def __mul__(self, other: DNA) -> DNA:
        return

    @classmethod
     