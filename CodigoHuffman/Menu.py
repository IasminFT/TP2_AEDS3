import os
import time
from Huffman import Huffman

class Menu:
    def __init__(self):
        self.huffman = Huffman()

    def apresentacao(self):
        print("(-)---------------------------------------------------------------(-)")
        print("          Curso de Sistemas de Informação - AEDS III")
        print("                     TRABALHO PRÁTICO 2")
        print("                      Código de Huffman")
        print("(-)---------------------------------------------------------------(-)")
        print("\nEste programa utiliza o código de Huffman para realizar a compressão e descompressão de textos.")
        print("Docente: Luciana\n")
        print("\nDiscentes:")
        print("Davy Garcia")
        print("Iasmin Torres")
        print("Lavínia Charrua")
        print("Lucas Cordeiro")
        print("Pedro Augusto")

    def exibir_menu(self):
        print("(-)----------------------------- Menu ----------------------------(-)")
        print("1. Compactar")
        print("2. Descompactar")
        print("3. Sair e Limpar")
        print("(-)---------------------------------------------------------------(-)")
        print()

    def executar(self):
        self.apresentacao()

        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção (1/2/3): ")

            if opcao == '1':
                self.compactar()
            elif opcao == '2':
                self.descompactar()
            elif opcao == '3':
                self.limpar_arquivos()
                print("Encerrando o programa e limpando arquivos. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def compactar(self):
        arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
        arquivo_saida = input("Digite o nome do arquivo de saída (.huf): ")
        if os.path.isfile(arquivo_entrada):
            texto = self.ler_arquivo(arquivo_entrada)
            start_time = time.time()
            self.huffman.comprimir(texto, arquivo_saida)
            end_time = time.time()
            print("--------------------------")
            print("Arquivo comprimido com sucesso!")
            print(f"Tempo de execução: {end_time - start_time:.2f} segundos\n")
        else:
            print(f"Erro: '{arquivo_entrada}' não é um arquivo válido.\n")

    def descompactar(self):
        arquivo_entrada = input("Digite o nome do arquivo de entrada (.huf): ")
        arquivo_saida = input("Digite o nome do arquivo de saída: ")
        if os.path.isfile(arquivo_entrada):
            start_time = time.time()
            texto_descomprimido = self.huffman.descomprimir_arquivo(arquivo_entrada, arquivo_saida)
            end_time = time.time()
            print("--------------------------")
            print("Arquivo descomprimido com sucesso!")
            print(f"Tempo de execução: {end_time - start_time:.2f} segundos\n")
            print("Texto descomprimido:")
            print(texto_descomprimido)
        else:
            print(f"Erro: '{arquivo_entrada}' não é um arquivo válido.\n")

    def ler_arquivo(self, nome_arquivo):
        try:
            print(f"Tentando abrir o arquivo: {os.path.abspath(nome_arquivo)}")
            with open(nome_arquivo, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Erro: '{nome_arquivo}' não é um arquivo válido.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar ler o arquivo '{nome_arquivo}': {e}")

    def limpar_arquivos(self):
        for file in os.listdir():
            if file.endswith(".txt") or file.endswith(".huf"):
                os.remove(file)
                print(f"Arquivo '{file}' removido.")
