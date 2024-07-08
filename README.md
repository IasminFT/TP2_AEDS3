## Algoritmos e Estrutura de Dados III

# Trabalho Prático 2
 
Docente: Luciana

Discentes:
 - Davy Garcia
 - Iasmin Torres
 - Lavínia Charrua
 - Lucas Cordeiro
 - Pedro Augusto
 
 # Código de Huffman - Compressão de Arquivos

Este programa Python implementa a codificação e decodificação de textos utilizando o algoritmo de Huffman. O algoritmo de Huffman é utilizado para compressão de dados, onde caracteres mais frequentes são representados por códigos binários menores.


### Requisitos:
- Python 3.x instalado

### Como usar:
1. #### Clone este repositório
       git clone https://github.com/seu-usuario/huffman-coding.git
       cd huffman-coding

2. #### Adicionando Arquivo 
    Adicione o arquivo de texto que você deseja compactar, ou o arquivo compactado que você deseja descompactar, na pasta       'TRABALHO PRATICO II AEDS 3'

3. #### Executando o Programa
   
   Execute o arquivo Main.py para iniciar o programa:
   `python Main.py`

4. #### Menu do Programa

    Ao executar `Main.py` você verá o seguinte menu:

       (-)------------------------------------------------------------------(-)
                      Curso de Sistemas de Informação - AEDS III
                                TRABALHO PRÁTICO 2
                                 Código de Huffman

       (-)----------------------------- Menu -------------------------------(-)
       1. Compactar
       2. Descompactar
       3. Sair e Limpar
       (-)------------------------------------------------------------------(-)
       
       Escolha uma opção (1/2/3):


  5. #### Opções do Menu
     - **Compactar** (`1`): Permite compactar um arquivo de texto digitando o nome do arquivo de entrada e o nome do arquivo de saída .huf.
     - **Descompactar** (`2`): Permite descompactar um arquivo .huf digitando o nome do arquivo de entrada e o nome do arquivo de saída.
     - **Sair e Limpar** (`3`): Encerra o programa e exclui todos os arquivos .txt e .huf criados durante a execução do programa.

-----------------------------------------------------------------------------------------------

### Observações
  - Certifique-se de ter os arquivos de texto que deseja compactar na mesma pasta que o `Main.py`.
  - Durante a compactação, será gerado um arquivo `.huf` como saída.
  - Durante a descompactação, será gerado um arquivo de texto como saída.
