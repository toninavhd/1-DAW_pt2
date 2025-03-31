class Dna:
    def __init__(self,sequence:str):
        self.sequence = sequence
        adenine = 'A'
        timine = 'T'
        guanine = 'G'
        citosine = 'C'

    def __len__(self) -> int:
        return len(self.sequence)
    
    def __str__(self) -> str:
        return print(self.sequence)