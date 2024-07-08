import os
from Huffman import Huffman

class Menu:
    def __init__(self):
        self.huffman = Huffman()

    def apresentacao(self):
        print("(-)---------------------------------------------------------------(-)")
        print("                Código de Huffman")
        print("            **Algoritmo e Estrutura de Dados**")
        print("(-)---------------------------------------------------------------(-)")
        print("\nEste programa realiza compressão e descompressão")
        print("de textos utilizando o algoritmo de Huffman.")
        print("\nIntegrantes:")
        print("1. [João Vitor Pinheiro]")
        print("2. [Thais Lopes]")
        print("3. [Hellen Gonçalves]")
        print("4. [Matheus Assis]")
        print("\nCurso de Sistemas de Informação - AEDS3")
        print("Professora: Luciana\n")

    def exibir_menu(self):
        print("(-)----------------------------- Menu ----------------------------(-)")
        print("1. Compactar")
        print("2. Descompactar")
        print("3. Sair")
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
                print("Encerrando o programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def compactar(self):
        arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
        arquivo_saida = input("Digite o nome do arquivo de saída (.huf): ")
        if os.path.isfile(arquivo_entrada):
            texto = self.ler_arquivo(arquivo_entrada)
            self.huffman.comprimir(texto, arquivo_saida)
            print("--------------------------")
            print("--------------------------")
            print("Arquivo comprimido com sucesso!\n")
            print()
        else:
            print(f"Erro: '{arquivo_entrada}' não é um arquivo válido.\n")
            print()

    def descompactar(self):
        arquivo_entrada = input("Digite o nome do arquivo de entrada (.huf): ")
        arquivo_saida = input("Digite o nome do arquivo de saída: ")
        if os.path.isfile(arquivo_entrada):
            texto_descomprimido = self.huffman.descomprimir_arquivo(arquivo_entrada, arquivo_saida)
            print("--------------------------")
            print("--------------------------")
            print("Arquivo descomprimido com sucesso!\n")
            print("Texto descomprimido:")
            print(texto_descomprimido)
            print()
            
        else:
            print(f"Erro: '{arquivo_entrada}' não é um arquivo válido.\n")
            print("(-)---------------------------------------------------------------(-)")
            print()
            print()

    def ler_arquivo(self, nome_arquivo):
        try:
            print(f"Tentando abrir o arquivo: {os.path.abspath(nome_arquivo)}")
            with open(nome_arquivo, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Erro: '{nome_arquivo}' não é um arquivo válido.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar ler o arquivo '{nome_arquivo}': {e}")
