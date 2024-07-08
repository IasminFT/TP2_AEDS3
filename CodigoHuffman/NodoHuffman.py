class NodoHuffman:
    def __init__(self, char=None, frequencia=None):
        self.char = char
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia
