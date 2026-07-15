'''
Implemente um sistema orientado a objetos em Python para
representar uma biblioteca com as classes Biblioteca, Livro,
Autor e Usuario, aplicando os conceitos de associação,
agregação, composição e dependência. A classe Autor deve
armazenar nome e nacionalidade; a classe Livro deve conter
título, ano e uma referência a um Autor (agregação). A Biblioteca
deve possuir um nome e ser responsável por criar e armazenar
os livros internamente (composição). A classe Usuario deve
conter o nome e manter uma referência à Biblioteca à qual está
associado (associação), além de possuir um método para pegar
um livro emprestado, usando temporariamente o livro sem
armazená-lo (dependência).
'''

class Biblioteca:
    '''Responsável por criar e armazenar os livros internamente (composição)'''
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__livros: list[Livro] = []

    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value) -> None:
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)
    
    def criar_livro(self, titulo: str, ano: int, autor: Autor) -> Livro:
        livro = Livro(titulo, ano, autor)
        self.__livros.append(livro)
        return livro
    
    def remover_livro(self, livro: Livro) -> None:
        self.__livros.remove(livro)

class Livro:
    def __init__(self, titulo: str, ano: int, autor: Autor) -> None:
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
    
    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value) -> None:
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)
    
class Autor:
    def __init__(self, nome: str, nacionalidade: str) -> None:
        self.__nome = nome
        self.__nacionalidade = nacionalidade
    
    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value) -> None:
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)

class Usuario:
    def __init__(self, nome: str, biblioteca: Biblioteca) -> None:
        self.__nome = nome
        self.__biblioteca = biblioteca
    
    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value) -> None:
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)
    
    def pegar_emprestado(self, livro: Livro):
        self.__biblioteca.remover_livro(livro)

# Interface
def exibir_menu(options: dict[str, tuple[str, function]]):
    for key, value in options.items():
        print(f"[{key}] {value[0]}")

def criar_usuario():
    print("\nCadastrar usuário")
    nome = input("Nome: ")
    usuario = Usuario(nome, biblioteca)

    print(f"\n{usuario.get("nome")} cadastrado(a) com sucesso!\n")

def criar_livro():
    print("\nCadastrar livro")
    titulo = input("Título: ")
    ano = int(input("Ano: "))
    nome = input("Autor: ")
    nacionalidade = input("Nacionalidade: ")

    autor = Autor(nome, nacionalidade)
    livro = biblioteca.criar_livro(titulo, ano, autor)

    print(f"\n{livro.get('titulo')} cadastrado com sucesso!\n")

def emprestar_livro():
    print("\nEmprestar livro")

def listar_livros():
    print("\nListar livros emprestados")

    for livro in biblioteca.get('livros'):
        titulo = livro.get('titulo')
        ano = livro.get('ano')
        autor = livro.get('autor').get('nome')
        print(f"{titulo} ({ano})\n{autor}")
        

if __name__ == "__main__":
    biblioteca = Biblioteca("A")
    criar_usuario()
    menu = {
            "1": ("Cadastrar livro", criar_livro),
            "2": ("Emprestar livro", emprestar_livro),
            "3": ("Listar livros", listar_livros),
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