class Livro:
    def __init__(self, titulo, autor, id):
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
    
    # -- Auxiliar
    def get(self, attr: str):
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value: str):
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)

class Usuario:
    def __init__(self, nome: str, matricula: int):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []

    # -- Auxiliar
    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")
    
    def set(self, attr: str, value: str) -> None:
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)

    # -- Consulta
    def pegar_livro_emprestado(self, livro) -> None:
        self.__livros_emprestados.append(livro)
        print(f"{self.__nome} pegou o livro {livro.get("titulo")} emprestado.")

    def devolver_livro(self, id_livro: int) -> None:
        for livro in self.__livros_emprestados:
            if livro.get("id") == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"\n{self.__nome} devolveu o livro '{livro.get("titulo")}'\n")
                return
        print(f"{self.__nome} não possui um livro com ID {id_livro}")
    
    def listar_livros_emprestados(self) -> None:
        if not self.__livros_emprestados:
            print(f"Nenhum livro emprestado.")
        else:
            print("\nLivros emprestados:")
            for livro in self.__livros_emprestados:
                print(f"- {livro.get("titulo")} (id: {livro.get("id")})")
            print()

# Interface
def exibir_menu(options: dict[str, tuple[str, function]]):
    for key, value in options.items():
        print(f"[{key}] {value[0]}")

def logar():
    usuario_id = input("Usuário (id)")
    global usuario_logado
    usuario_logado = usuarios[usuario_id]

def deslogar():
    global usuario_logado
    usuario_logado = None

def criar_usuario():
    print("\nCadastrar usuário")
    nome = input("Nome: ")
    usuario = Usuario(nome, len(usuarios) + 1)
    usuarios[usuario.get("matricula")] = usuario

    print(f"\n{usuario.get("nome")} cadastrado(a) com sucesso!\n")

    escolha = input("Entrar com o usuário criado?\n[1] Sim\n[2] Não\nEscolha: ")
    if escolha == "1":
        global usuario_logado
        usuario_logado = usuario

def criar_livro():
    print("\nCadastrar livro")
    titulo = input("Título: ")
    autor = input("Autor: ")
    livro = Livro(titulo, autor, len(livros) + 1)
    livros[livro.get("id")] = livro
    print(f"\n{livro.get("titulo")} cadastrado com sucesso!\n")

def emprestar_livro():
    print("\nEmprestar livro")
    if not usuario_logado:
        usuario_id = int(input("Usuário (ID): "))

    usuario = usuario_logado or usuarios[usuario_id]
    
    livro_id = int(input("Livro (ID): "))
    livro = livros[livro_id]

    usuario.pegar_livro_emprestado(livro)
    
def devolver_livro():
    print("\nDevolver livro")
    if not usuario_logado:
        usuario_id = int(input("Usuário (ID): "))
    livro_id = int(input("Livro (ID): "))
    
    usuario = usuario_logado or usuarios[usuario_id]
    usuario.devolver_livro(livro_id)

def listar_livros_emprestados():
    print("\nListar livros emprestados")
    if not usuario_logado:
        usuario_id = int(input("Usuário (ID): "))

    usuario = usuario_logado or usuarios[usuario_id]
    usuario.listar_livros_emprestados()

if __name__ == "__main__":
    usuarios = {}
    usuario_logado = None
    livros = {}
    menu = {
        "1": ("Cadastrar livro", criar_livro),
        "2": ("Cadastrar usuário", criar_usuario),
        "3": ("Emprestar livro", emprestar_livro),
        "4": ("Devolver livro", devolver_livro),
        "5": ("Listar livros emprestados", listar_livros_emprestados),
        "6": ("Login", logar),
        "7": ("Logout", deslogar),
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