from collections import defaultdict
from NodoHuffman import NodoHuffman
import heapq

class Huffman:
    def __init__(self):
        self.heap = []  # Adicionei o atributo 'heap'

    def _construir_dicionario_frequencia(self, texto):
        freq_dict = {}
        for char in texto:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        return freq_dict

    def _construir_arvore_huffman(self, freq_dict):
        for char, freq in freq_dict.items():
            heapq.heappush(self.heap, NodoHuffman(char, freq))

        while len(self.heap) > 1:
            esquerda = heapq.heappop(self.heap)
            direita = heapq.heappop(self.heap)
            nodo_merge = NodoHuffman(None, esquerda.frequencia + direita.frequencia)
            nodo_merge.esquerda = esquerda
            nodo_merge.direita = direita
            heapq.heappush(self.heap, nodo_merge)

        return self.heap[0]

    def _construir_codigos_huffman(self, nodo, codigo_atual, codigos):
        if nodo is not None:
            if nodo.char is not None:
                codigos[nodo.char] = codigo_atual
            self._construir_codigos_huffman(nodo.esquerda, codigo_atual + '0', codigos)
            self._construir_codigos_huffman(nodo.direita, codigo_atual + '1', codigos)

    def comprimir(self, texto, arquivo_saida):
        freq_dict = self._construir_dicionario_frequencia(texto)
        raiz = self._construir_arvore_huffman(freq_dict)
        codigos = {}
        self._construir_codigos_huffman(raiz, '', codigos)

        texto_codificado = ''.join([codigos[char] for char in texto])
        padding = 8 - (len(texto_codificado) % 8)
        texto_codificado += '0' * padding
        info_padding = format(padding, '08b')
        texto_codificado = info_padding + texto_codificado

        bytes_array = bytearray()
        for i in range(0, len(texto_codificado), 8):
            byte = texto_codificado[i:i + 8]
            bytes_array.append(int(byte, 2))

        with open(arquivo_saida, 'wb') as f:
            f.write(bytes(bytes_array))

    def descomprimir(self, input_file, output_file):
        with open(input_file, 'rb') as f:
            byte_array = f.read()

        padding = int(byte_array[0] & 0x0F)
        encoded_text = ''.join([format(byte, '08b') for byte in byte_array[1:]])

        encoded_text = encoded_text[:-padding] if padding > 0 else encoded_text

        if not self.heap:
            self.heap.append(self.construir_arvore(encoded_text))

        current_node = self.heap[0]
        decoded_text = []

        for bit in encoded_text:
            if bit == '0':
                current_node = current_node.esquerda
            else:
                current_node = current_node.direita

            if current_node.char is not None:
                decoded_text.append(current_node.char)
                current_node = self.heap[0]

        decoded_text = ''.join(decoded_text)

        with open(output_file, 'w') as f:
            f.write(decoded_text)

        self.imprimir_arvore(self.heap[0], 0)  # Adicionando impressão da árvore

        return decoded_text
    
    def construir_arvore(self, encoded_text):
        frequencias = defaultdict(int)
        for bit in encoded_text:
            frequencias[bit] += 1

        heap = [NodoHuffman(char=char, frequencia=frequencia) for char, frequencia in frequencias.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            no_esquerdo = heapq.heappop(heap)
            no_direito = heapq.heappop(heap)

            novo_no = NodoHuffman(frequencia=no_esquerdo.frequencia + no_direito.frequencia)
            novo_no.esquerda = no_esquerdo
            novo_no.direita = no_direito

            heapq.heappush(heap, novo_no)

        return heap[0]

    def imprimir_arvore(self, no, nivel):
        if no is not None:
            self.imprimir_arvore(no.direita, nivel + 1)
            print(' ' * 4 * nivel + '──', no.char, f"({no.frequencia})")
            self.imprimir_arvore(no.esquerda, nivel + 1)

    # Função para descomprimir um arquivo e retornar o texto original
    def descomprimir_arquivo(self, input_file, output_file):
        texto_descomprimido = self.descomprimir(input_file, output_file)
        return texto_descomprimido
