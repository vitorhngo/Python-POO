'''
5. Implemente uma classe Impressora com o método
imprimir(Documento d), que recebe um objeto da classe
Documento e imprime suas informações na tela. A classe
Documento deve conter os atributos título e conteúdo. A
classe Impressora apenas utiliza o documento, sem manter
uma referência permanente a ele, caracterizando uma relação
de dependência. Desenvolva um programa com um menu
interativo no console que permita criar vários documentos,
visualizar seu conteúdo por meio da impressora e encerrar o
programa.
'''
import time

class Impressora():
    duracao = 5
    def imprimir(self, documento: Documento) -> Documento:
        print(f"Imprimindo: {documento.get('titulo')}")
        print("...")
        time.sleep(self.duracao)
        print(f"Conteúdo:\n{documento.get('conteudo')}")
        return documento

class Documento():
    def __init__(self, titulo: str, conteudo: str) -> None:
        self.set_titulo(titulo)
        self.set_conteudo(conteudo)
        
    def set_titulo(self, valor: str) -> str:
        if len(valor) < 3:
            raise ValueError("Título não pode ter menos que 3 caracteres.")
        
        self.__titulo = valor
        return self.__titulo
    
    def set_conteudo(self, valor: str) -> str:
        if len(valor) > 500:
            raise ValueError("Conteúdo não pode ter mais que 500 caracteres.")
        
        self.__conteudo = valor
        return self.__conteudo

    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

# Interface
def exibir_menu(options: dict[str, tuple[str, function]]) -> None:
    for key, value in options.items():
        print(f"[{key}] {value[0]}")

def criar_documento() -> None:
    print("\nCriar documento:\n")
    documento = Documento("   ", "")
    try: 
        titulo = input("Título: ")
        documento.set_titulo(titulo)

        conteudo = input("Conteúdo: ")
        documento.set_conteudo(conteudo)
    except ValueError as e:
        print("\nERRO!")
        print(e)
    else:
        id = str(len(documentos) + 1)
        documentos[id] = documento

def listar_documentos() -> None:
    if not documentos:
        print("\nNão há documentos para listar.")
        return
    print("(ID) Título")
    print("\nDocumentos:\n")
    for id, documento in documentos.items():
        print(f"({id}) {documento.get('titulo')}")

def imprimir_documento() -> None:
    if not documentos:
        print("\nNão há documentos para imprimir.")
        return
    print("\nImprimir documento:\n")
    listar_documentos()
    id = input("\nDocumento (ID): ")
    documento = documentos[id]
    Impressora().imprimir(documento)
    
if __name__ == "__main__":
    documentos: dict[str, Documento] = {}
    menu = {
        "1": ("Criar documento", criar_documento),
        "2": ("Listar documentos", listar_documentos),
        "3": ("Imprimir", imprimir_documento),
        "0": ("Sair", quit)
    }
    
    while True:
        print()
        exibir_menu(menu)
        escolha = input("Escolha: ")
        try:
            menu[escolha][1]()
        except KeyError as e:
            print("Escolha uma opção válida.")