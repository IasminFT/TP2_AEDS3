from Huffman import Huffman
from Menu import Menu  

class Main:
    @staticmethod
    def main():
        menu = Menu()
        menu.executar()

        # Exemplo de descompressão de arquivo após o uso do menu
        huffman = Huffman()  # Crie uma instância da classe Huffman
        arquivo_entrada = "saida.huf"  # Substitua pelo nome do seu arquivo de entrada .huf
        arquivo_saida = "entrada.txt"  # Substitua pelo nome desejado para o arquivo de saída .txt

        texto_original = Huffman.descomprimir_arquivo(arquivo_entrada, arquivo_saida)

        print("Texto original descomprimido:")
        print(texto_original)

if __name__ == "__main__":
    Main.main()
